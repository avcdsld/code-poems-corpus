def _at_least_x_are_true(a, b, x):
  """At least `x` of `a` and `b` `Tensors` are true."""
  match = tf.equal(a, b)
  match = tf.cast(match, tf.int32)
  return tf.greater_equal(tf.reduce_sum(match), x)