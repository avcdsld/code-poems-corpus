def awaitTermination(self, timeout=None):
        """
        Wait for the execution to stop.

        @param timeout: time to wait in seconds
        """
        if timeout is None:
            self._jssc.awaitTermination()
        else:
            self._jssc.awaitTerminationOrTimeout(int(timeout * 1000))