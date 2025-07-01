def CompressedHistograms(self, run, tag):
    """Retrieve the compressed histogram events associated with a run and tag.

    Args:
      run: A string name of the run for which values are retrieved.
      tag: A string name of the tag for which values are retrieved.

    Raises:
      KeyError: If the run is not found, or the tag is not available for
        the given run.

    Returns:
      An array of `event_accumulator.CompressedHistogramEvents`.
    """
    accumulator = self.GetAccumulator(run)
    return accumulator.CompressedHistograms(tag)