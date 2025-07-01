def reset(self, indices=None):
    """Reset the batch of environments.

    Args:
      indices: The batch indices of the environments to reset.

    Returns:
      Batch tensor of the new observations.
    """
    return tf.cond(
        tf.cast(tf.reduce_sum(indices + 1), tf.bool),
        lambda: self._reset_non_empty(indices),
        lambda: tf.cast(0, self.observ_dtype))