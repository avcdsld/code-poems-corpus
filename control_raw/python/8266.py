def start_ray_processes(self):
        """Start all of the processes on the node."""
        logger.info(
            "Process STDOUT and STDERR is being redirected to {}.".format(
                self._logs_dir))

        self.start_plasma_store()
        self.start_raylet()
        if PY3:
            self.start_reporter()

        if self._ray_params.include_log_monitor:
            self.start_log_monitor()