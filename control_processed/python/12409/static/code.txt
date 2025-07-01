def set_close_callback(self, callback: Optional[Callable[[], None]]) -> None:
        """Call the given callback when the stream is closed.

        This mostly is not necessary for applications that use the
        `.Future` interface; all outstanding ``Futures`` will resolve
        with a `StreamClosedError` when the stream is closed. However,
        it is still useful as a way to signal that the stream has been
        closed while no other read or write is in progress.

        Unlike other callback-based interfaces, ``set_close_callback``
        was not removed in Tornado 6.0.
        """
        self._close_callback = callback
        self._maybe_add_error_listener()