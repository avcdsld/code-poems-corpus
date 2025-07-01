def dropout_no_scaling(x, keep_prob):
  """Like tf.nn.dropout, but does not scale up.  Works on integers also.

  Args:
    x: a Tensor
    keep_prob: a floating point number

  Returns:
    Tensor of the same shape as x.
  """
  if keep_prob == 1.0:
    return x
  mask = tf.less(tf.random_uniform(tf.shape(x)), keep_prob)
  return x * cast_like(mask, x)