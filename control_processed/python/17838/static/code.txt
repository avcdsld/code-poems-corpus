def refresh(self, line=None):
        """Refreshes progress bar."""
        # Just go away if it is locked. Will update next time
        if not self._lock.acquire(False):
            return

        if line is None:
            line = self._line

        if sys.stdout.isatty() and line is not None:
            self._writeln(line)
            self._line = line

        self._lock.release()