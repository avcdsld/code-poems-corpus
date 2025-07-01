def run_until_shutdown(self):
        ''' Run the Bokeh Server until shutdown is requested by the user,
        either via a Keyboard interrupt (Ctrl-C) or SIGTERM.

        Calling this method will start the Tornado ``IOLoop`` and block
        all execution in the calling process.

        Returns:
            None

        '''
        if not self._started:
            self.start()
        # Install shutdown hooks
        atexit.register(self._atexit)
        signal.signal(signal.SIGTERM, self._sigterm)
        try:
            self._loop.start()
        except KeyboardInterrupt:
            print("\nInterrupted, shutting down")
        self.stop()