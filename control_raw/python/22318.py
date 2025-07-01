def remove(self, handler_id=None):
        """Remove a previously added handler and stop sending logs to its sink.

        Parameters
        ----------
        handler_id : |int| or ``None``
            The id of the sink to remove, as it was returned by the |add| method. If ``None``, all
            handlers are removed. The pre-configured handler is guaranteed to have the index ``0``.

        Raises
        ------
        ValueError
            If ``handler_id`` is not ``None`` but there is no active handler with such id.

        Examples
        --------
        >>> i = logger.add(sys.stderr, format="{message}")
        >>> logger.info("Logging")
        Logging
        >>> logger.remove(i)
        >>> logger.info("No longer logging")
        """
        with self._lock:
            handlers = self._handlers.copy()

            if handler_id is None:
                for handler in handlers.values():
                    handler.stop()
                handlers.clear()
            else:
                try:
                    handler = handlers.pop(handler_id)
                except KeyError:
                    raise ValueError("There is no existing handler with id '%s'" % handler_id)
                handler.stop()

            levelnos = (h.levelno for h in handlers.values())
            self.__class__._min_level = min(levelnos, default=float("inf"))
            self.__class__._handlers = handlers