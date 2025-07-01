def kill_plasma_store(self, check_alive=True):
        """Kill the plasma store.

        Args:
            check_alive (bool): Raise an exception if the process was already
                dead.
        """
        self._kill_process_type(
            ray_constants.PROCESS_TYPE_PLASMA_STORE, check_alive=check_alive)