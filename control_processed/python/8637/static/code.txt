def fetch_and_register_remote_function(self, key):
        """Import a remote function."""
        (driver_id_str, function_id_str, function_name, serialized_function,
         num_return_vals, module, resources,
         max_calls) = self._worker.redis_client.hmget(key, [
             "driver_id", "function_id", "name", "function", "num_return_vals",
             "module", "resources", "max_calls"
         ])
        function_id = ray.FunctionID(function_id_str)
        driver_id = ray.DriverID(driver_id_str)
        function_name = decode(function_name)
        max_calls = int(max_calls)
        module = decode(module)

        # This is a placeholder in case the function can't be unpickled. This
        # will be overwritten if the function is successfully registered.
        def f():
            raise Exception("This function was not imported properly.")

        # This function is called by ImportThread. This operation needs to be
        # atomic. Otherwise, there is race condition. Another thread may use
        # the temporary function above before the real function is ready.
        with self.lock:
            self._function_execution_info[driver_id][function_id] = (
                FunctionExecutionInfo(
                    function=f,
                    function_name=function_name,
                    max_calls=max_calls))
            self._num_task_executions[driver_id][function_id] = 0

            try:
                function = pickle.loads(serialized_function)
            except Exception:
                # If an exception was thrown when the remote function was
                # imported, we record the traceback and notify the scheduler
                # of the failure.
                traceback_str = format_error_message(traceback.format_exc())
                # Log the error message.
                push_error_to_driver(
                    self._worker,
                    ray_constants.REGISTER_REMOTE_FUNCTION_PUSH_ERROR,
                    "Failed to unpickle the remote function '{}' with "
                    "function ID {}. Traceback:\n{}".format(
                        function_name, function_id.hex(), traceback_str),
                    driver_id=driver_id)
            else:
                # The below line is necessary. Because in the driver process,
                # if the function is defined in the file where the python
                # script was started from, its module is `__main__`.
                # However in the worker process, the `__main__` module is a
                # different module, which is `default_worker.py`
                function.__module__ = module
                self._function_execution_info[driver_id][function_id] = (
                    FunctionExecutionInfo(
                        function=function,
                        function_name=function_name,
                        max_calls=max_calls))
                # Add the function to the function table.
                self._worker.redis_client.rpush(
                    b"FunctionTable:" + function_id.binary(),
                    self._worker.worker_id)