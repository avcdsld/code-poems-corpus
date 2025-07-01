def get(self, mode, metric):
    """Get the history for the given metric and mode."""
    if mode not in self._values:
      logging.info("Metric %s not found for mode %s", metric, mode)
      return []
    return list(self._values[mode][metric])