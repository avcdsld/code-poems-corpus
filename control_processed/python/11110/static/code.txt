def update(self, n=1):
    """Increment current value."""
    with self._lock:
      self._pbar.update(n)
      self.refresh()