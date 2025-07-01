def connect(node,
            mode=WORKER_MODE,
            log_to_driver=False,
            worker=global_worker,
            driver_id=None,
            load_code_from_local=False):
    """Connect this worker to the raylet, to Plasma, and to Redis.

    Args:
        node (ray.node.Node): The node to connect.
        mode: The mode of the worker. One of SCRIPT_MODE, WORKER_MODE, and
            LOCAL_MODE.
        log_to_driver (bool): If true, then output from all of the worker
            processes on all nodes will be directed to the driver.
        worker: The ray.Worker instance.
        driver_id: The ID of driver. If it's None, then we will generate one.
    """
    # Do some basic checking to make sure we didn't call ray.init twice.
    error_message = "Perhaps you called ray.init twice by accident?"
    assert not worker.connected, error_message
    assert worker.cached_functions_to_run is not None, error_message

    # Enable nice stack traces on SIGSEGV etc.
    if not faulthandler.is_enabled():
        faulthandler.enable(all_threads=False)

    worker.profiler = profiling.Profiler(worker, worker.threads_stopped)

    # Initialize some fields.
    if mode is WORKER_MODE:
        worker.worker_id = _random_string()
        if setproctitle:
            setproctitle.setproctitle("ray_worker")
    else:
        # This is the code path of driver mode.
        if driver_id is None:
            driver_id = DriverID(_random_string())

        if not isinstance(driver_id, DriverID):
            raise TypeError("The type of given driver id must be DriverID.")

        worker.worker_id = driver_id.binary()

    # When tasks are executed on remote workers in the context of multiple
    # drivers, the task driver ID is used to keep track of which driver is
    # responsible for the task so that error messages will be propagated to
    # the correct driver.
    if mode != WORKER_MODE:
        worker.task_driver_id = DriverID(worker.worker_id)

    # All workers start out as non-actors. A worker can be turned into an actor
    # after it is created.
    worker.actor_id = ActorID.nil()
    worker.node = node
    worker.set_mode(mode)

    # If running Ray in LOCAL_MODE, there is no need to create call
    # create_worker or to start the worker service.
    if mode == LOCAL_MODE:
        return

    # Create a Redis client.
    # The Redis client can safely be shared between threads. However, that is
    # not true of Redis pubsub clients. See the documentation at
    # https://github.com/andymccurdy/redis-py#thread-safety.
    worker.redis_client = node.create_redis_client()

    # For driver's check that the version information matches the version
    # information that the Ray cluster was started with.
    try:
        ray.services.check_version_info(worker.redis_client)
    except Exception as e:
        if mode == SCRIPT_MODE:
            raise e
        elif mode == WORKER_MODE:
            traceback_str = traceback.format_exc()
            ray.utils.push_error_to_driver_through_redis(
                worker.redis_client,
                ray_constants.VERSION_MISMATCH_PUSH_ERROR,
                traceback_str,
                driver_id=None)

    worker.lock = threading.RLock()

    # Create an object for interfacing with the global state.
    global_state._initialize_global_state(
        node.redis_address, redis_password=node.redis_password)

    # Register the worker with Redis.
    if mode == SCRIPT_MODE:
        # The concept of a driver is the same as the concept of a "job".
        # Register the driver/job with Redis here.
        import __main__ as main
        driver_info = {
            "node_ip_address": node.node_ip_address,
            "driver_id": worker.worker_id,
            "start_time": time.time(),
            "plasma_store_socket": node.plasma_store_socket_name,
            "raylet_socket": node.raylet_socket_name,
            "name": (main.__file__
                     if hasattr(main, "__file__") else "INTERACTIVE MODE")
        }
        worker.redis_client.hmset(b"Drivers:" + worker.worker_id, driver_info)
    elif mode == WORKER_MODE:
        # Register the worker with Redis.
        worker_dict = {
            "node_ip_address": node.node_ip_address,
            "plasma_store_socket": node.plasma_store_socket_name,
        }
        # Check the RedirectOutput key in Redis and based on its value redirect
        # worker output and error to their own files.
        # This key is set in services.py when Redis is started.
        redirect_worker_output_val = worker.redis_client.get("RedirectOutput")
        if (redirect_worker_output_val is not None
                and int(redirect_worker_output_val) == 1):
            log_stdout_file, log_stderr_file = (
                node.new_worker_redirected_log_file(worker.worker_id))
            # Redirect stdout/stderr at the file descriptor level. If we simply
            # set sys.stdout and sys.stderr, then logging from C++ can fail to
            # be redirected.
            os.dup2(log_stdout_file.fileno(), sys.stdout.fileno())
            os.dup2(log_stderr_file.fileno(), sys.stderr.fileno())
            # We also manually set sys.stdout and sys.stderr because that seems
            # to have an affect on the output buffering. Without doing this,
            # stdout and stderr are heavily buffered resulting in seemingly
            # lost logging statements.
            sys.stdout = log_stdout_file
            sys.stderr = log_stderr_file
            # This should always be the first message to appear in the worker's
            # stdout and stderr log files. The string "Ray worker pid:" is
            # parsed in the log monitor process.
            print("Ray worker pid: {}".format(os.getpid()))
            print("Ray worker pid: {}".format(os.getpid()), file=sys.stderr)
            sys.stdout.flush()
            sys.stderr.flush()

            worker_dict["stdout_file"] = os.path.abspath(log_stdout_file.name)
            worker_dict["stderr_file"] = os.path.abspath(log_stderr_file.name)
        worker.redis_client.hmset(b"Workers:" + worker.worker_id, worker_dict)
    else:
        raise Exception("This code should be unreachable.")

    # Create an object store client.
    worker.plasma_client = thread_safe_client(
        plasma.connect(node.plasma_store_socket_name, None, 0, 300))

    # If this is a driver, set the current task ID, the task driver ID, and set
    # the task index to 0.
    if mode == SCRIPT_MODE:
        # If the user provided an object_id_seed, then set the current task ID
        # deterministically based on that seed (without altering the state of
        # the user's random number generator). Otherwise, set the current task
        # ID randomly to avoid object ID collisions.
        numpy_state = np.random.get_state()
        if node.object_id_seed is not None:
            np.random.seed(node.object_id_seed)
        else:
            # Try to use true randomness.
            np.random.seed(None)
        # Reset the state of the numpy random number generator.
        np.random.set_state(numpy_state)

        # Create an entry for the driver task in the task table. This task is
        # added immediately with status RUNNING. This allows us to push errors
        # related to this driver task back to the driver.  For example, if the
        # driver creates an object that is later evicted, we should notify the
        # user that we're unable to reconstruct the object, since we cannot
        # rerun the driver.
        nil_actor_counter = 0

        function_descriptor = FunctionDescriptor.for_driver_task()
        driver_task = ray._raylet.Task(
            worker.task_driver_id,
            function_descriptor.get_function_descriptor_list(),
            [],  # arguments.
            0,  # num_returns.
            TaskID(_random_string()),  # parent_task_id.
            0,  # parent_counter.
            ActorID.nil(),  # actor_creation_id.
            ObjectID.nil(),  # actor_creation_dummy_object_id.
            0,  # max_actor_reconstructions.
            ActorID.nil(),  # actor_id.
            ActorHandleID.nil(),  # actor_handle_id.
            nil_actor_counter,  # actor_counter.
            [],  # new_actor_handles.
            [],  # execution_dependencies.
            {},  # resource_map.
            {},  # placement_resource_map.
        )

        # Add the driver task to the task table.
        global_state._execute_command(driver_task.task_id(), "RAY.TABLE_ADD",
                                      ray.gcs_utils.TablePrefix.RAYLET_TASK,
                                      ray.gcs_utils.TablePubsub.RAYLET_TASK,
                                      driver_task.task_id().binary(),
                                      driver_task._serialized_raylet_task())

        # Set the driver's current task ID to the task ID assigned to the
        # driver task.
        worker.task_context.current_task_id = driver_task.task_id()

    worker.raylet_client = ray._raylet.RayletClient(
        node.raylet_socket_name,
        ClientID(worker.worker_id),
        (mode == WORKER_MODE),
        DriverID(worker.current_task_id.binary()),
    )

    # Start the import thread
    worker.import_thread = import_thread.ImportThread(worker, mode,
                                                      worker.threads_stopped)
    worker.import_thread.start()

    # If this is a driver running in SCRIPT_MODE, start a thread to print error
    # messages asynchronously in the background. Ideally the scheduler would
    # push messages to the driver's worker service, but we ran into bugs when
    # trying to properly shutdown the driver's worker service, so we are
    # temporarily using this implementation which constantly queries the
    # scheduler for new error messages.
    if mode == SCRIPT_MODE:
        q = queue.Queue()
        worker.listener_thread = threading.Thread(
            target=listen_error_messages_raylet,
            name="ray_listen_error_messages",
            args=(worker, q, worker.threads_stopped))
        worker.printer_thread = threading.Thread(
            target=print_error_messages_raylet,
            name="ray_print_error_messages",
            args=(q, worker.threads_stopped))
        worker.listener_thread.daemon = True
        worker.listener_thread.start()
        worker.printer_thread.daemon = True
        worker.printer_thread.start()
        if log_to_driver:
            worker.logger_thread = threading.Thread(
                target=print_logs,
                name="ray_print_logs",
                args=(worker.redis_client, worker.threads_stopped))
            worker.logger_thread.daemon = True
            worker.logger_thread.start()

    # If we are using the raylet code path and we are not in local mode, start
    # a background thread to periodically flush profiling data to the GCS.
    if mode != LOCAL_MODE:
        worker.profiler.start_flush_thread()

    if mode == SCRIPT_MODE:
        # Add the directory containing the script that is running to the Python
        # paths of the workers. Also add the current directory. Note that this
        # assumes that the directory structures on the machines in the clusters
        # are the same.
        script_directory = os.path.abspath(os.path.dirname(sys.argv[0]))
        current_directory = os.path.abspath(os.path.curdir)
        worker.run_function_on_all_workers(
            lambda worker_info: sys.path.insert(1, script_directory))
        worker.run_function_on_all_workers(
            lambda worker_info: sys.path.insert(1, current_directory))
        # TODO(rkn): Here we first export functions to run, then remote
        # functions. The order matters. For example, one of the functions to
        # run may set the Python path, which is needed to import a module used
        # to define a remote function. We may want to change the order to
        # simply be the order in which the exports were defined on the driver.
        # In addition, we will need to retain the ability to decide what the
        # first few exports are (mostly to set the Python path). Additionally,
        # note that the first exports to be defined on the driver will be the
        # ones defined in separate modules that are imported by the driver.
        # Export cached functions_to_run.
        for function in worker.cached_functions_to_run:
            worker.run_function_on_all_workers(function)
        # Export cached remote functions and actors to the workers.
        worker.function_actor_manager.export_cached()
    worker.cached_functions_to_run = None