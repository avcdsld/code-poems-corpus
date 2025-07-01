def on_set(self, key, value):
    """Callback called on successful set. Uses function from __init__."""
    if self._on_set is not None:
      self._on_set(key, value)