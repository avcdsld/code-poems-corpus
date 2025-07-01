def _CheckForOutOfOrderStepAndMaybePurge(self, event):
    """Check for out-of-order event.step and discard expired events for tags.

    Check if the event is out of order relative to the global most recent step.
    If it is, purge outdated summaries for tags that the event contains.

    Args:
      event: The event to use as reference. If the event is out-of-order, all
        events with the same tags, but with a greater event.step will be purged.
    """
    if event.step < self.most_recent_step and event.HasField('summary'):
      self._Purge(event, by_tags=True)