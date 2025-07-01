def expand_batch_coordinates(bc, length_factor):
  """Duplicate elements of bc by length_factor.

  Args:
    bc (tf.Tensor): int32 tensor of shape [1, length, 1]
    length_factor (int):

  Returns:
    tf.Tensor: of shape [1, length*length_factor, 1] where every elements has
      been duplicated length_factor times.
  """
  assert bc.get_shape().as_list() == [1, None, 1]
  # bc has shape [1, length, 1]
  bc *= tf.constant([[1] * length_factor])
  # bc has shape [1, length, length_factor]
  bc = tf.reshape(bc, [1, -1, 1])
  # bc has shape [1, length*length_factor]
  return bc