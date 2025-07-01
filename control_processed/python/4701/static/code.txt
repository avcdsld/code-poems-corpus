def reset(self, indices=None):
    """Resets environments at given indices.

    Subclasses should override _reset to do the actual reset if something other
    than the default implementation is desired.

    Args:
      indices: Indices of environments to reset. If None all envs are reset.

    Returns:
      Batch of initial observations of reset environments.
    """

    if indices is None:
      indices = np.arange(self.trajectories.batch_size)

    # If this is empty (not None) then don't do anything, no env was done.
    if indices.size == 0:
      tf.logging.warning(
          "`reset` called with empty indices array, this is a no-op.")
      return None

    observations = self._reset(indices)
    processed_observations = self.process_observations(observations)

    # Record history.
    self.trajectories.reset(indices, observations)

    return processed_observations