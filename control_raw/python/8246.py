def _process_task(self, task, function_execution_info):
        """Execute a task assigned to this worker.

        This method deserializes a task from the scheduler, and attempts to
        execute the task. If the task succeeds, the outputs are stored in the
        local object store. If the task throws an exception, RayTaskError
        objects are stored in the object store to represent the failed task
        (these will be retrieved by calls to get or by subsequent tasks that
        use the outputs of this task).
        """
        assert self.current_task_id.is_nil()
        assert self.task_context.task_index == 0
        assert self.task_context.put_index == 1
        if task.actor_id().is_nil():
            # If this worker is not an actor, check that `task_driver_id`
            # was reset when the worker finished the previous task.
            assert self.task_driver_id.is_nil()
            # Set the driver ID of the current running task. This is
            # needed so that if the task throws an exception, we propagate
            # the error message to the correct driver.
            self.task_driver_id = task.driver_id()
        else:
            # If this worker is an actor, task_driver_id wasn't reset.
            # Check that current task's driver ID equals the previous one.
            assert self.task_driver_id == task.driver_id()

        self.task_context.current_task_id = task.task_id()

        function_descriptor = FunctionDescriptor.from_bytes_list(
            task.function_descriptor_list())
        args = task.arguments()
        return_object_ids = task.returns()
        if (not task.actor_id().is_nil()
                or not task.actor_creation_id().is_nil()):
            dummy_return_id = return_object_ids.pop()
        function_executor = function_execution_info.function
        function_name = function_execution_info.function_name

        # Get task arguments from the object store.
        try:
            if function_name != "__ray_terminate__":
                self.reraise_actor_init_error()
            self.memory_monitor.raise_if_low_memory()
            with profiling.profile("task:deserialize_arguments"):
                arguments = self._get_arguments_for_execution(
                    function_name, args)
        except Exception as e:
            self._handle_process_task_failure(
                function_descriptor, return_object_ids, e,
                ray.utils.format_error_message(traceback.format_exc()))
            return

        # Execute the task.
        try:
            self._current_task = task
            with profiling.profile("task:execute"):
                if (task.actor_id().is_nil()
                        and task.actor_creation_id().is_nil()):
                    outputs = function_executor(*arguments)
                else:
                    if not task.actor_id().is_nil():
                        key = task.actor_id()
                    else:
                        key = task.actor_creation_id()
                    outputs = function_executor(dummy_return_id,
                                                self.actors[key], *arguments)
        except Exception as e:
            # Determine whether the exception occured during a task, not an
            # actor method.
            task_exception = task.actor_id().is_nil()
            traceback_str = ray.utils.format_error_message(
                traceback.format_exc(), task_exception=task_exception)
            self._handle_process_task_failure(
                function_descriptor, return_object_ids, e, traceback_str)
            return
        finally:
            self._current_task = None

        # Store the outputs in the local object store.
        try:
            with profiling.profile("task:store_outputs"):
                # If this is an actor task, then the last object ID returned by
                # the task is a dummy output, not returned by the function
                # itself. Decrement to get the correct number of return values.
                num_returns = len(return_object_ids)
                if num_returns == 1:
                    outputs = (outputs, )
                self._store_outputs_in_object_store(return_object_ids, outputs)
        except Exception as e:
            self._handle_process_task_failure(
                function_descriptor, return_object_ids, e,
                ray.utils.format_error_message(traceback.format_exc()))