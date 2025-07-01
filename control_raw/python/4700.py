def _reset(self, indices):
    """Resets environments at indices shouldn't pre-process or record.

    Subclasses should override this to do the actual reset if something other
    than the default implementation is desired.

    Args:
      indices: list of indices of underlying envs to call reset on.

    Returns:
      np.ndarray of stacked observations from the reset-ed envs.
    """

    # Pre-conditions: common_preconditions, see `assert_common_preconditions`.
    self.assert_common_preconditions()

    # This returns a numpy array with first dimension `len(indices)` and the
    # rest being the dimensionality of the observation.
    return np.stack([self._envs[index].reset() for index in indices])