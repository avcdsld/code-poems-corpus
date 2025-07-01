def close(self, reason=None):
        """Stop consuming messages and shutdown all helper threads.

        This method is idempotent. Additional calls will have no effect.

        Args:
            reason (Any): The reason to close this. If None, this is considered
                an "intentional" shutdown. This is passed to the callbacks
                specified via :meth:`add_close_callback`.
        """
        with self._closing:
            if self._closed:
                return

            # Stop consuming messages.
            if self.is_active:
                _LOGGER.debug("Stopping consumer.")
                self._consumer.stop()
            self._consumer = None

            # Shutdown all helper threads
            _LOGGER.debug("Stopping scheduler.")
            self._scheduler.shutdown()
            self._scheduler = None
            _LOGGER.debug("Stopping leaser.")
            self._leaser.stop()
            self._leaser = None
            _LOGGER.debug("Stopping dispatcher.")
            self._dispatcher.stop()
            self._dispatcher = None
            _LOGGER.debug("Stopping heartbeater.")
            self._heartbeater.stop()
            self._heartbeater = None

            self._rpc = None
            self._closed = True
            _LOGGER.debug("Finished stopping manager.")

            for callback in self._close_callbacks:
                callback(self, reason)