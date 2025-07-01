def shutdown(self):
        """Shuts down the scheduler and immediately end all pending callbacks.
        """
        # Drop all pending item from the executor. Without this, the executor
        # will block until all pending items are complete, which is
        # undesirable.
        try:
            while True:
                self._executor._work_queue.get(block=False)
        except queue.Empty:
            pass
        self._executor.shutdown()