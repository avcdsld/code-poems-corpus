def flatten_all_but_last(a):
  """Flatten all dimensions of a except the last."""
  ret = tf.reshape(a, [-1, tf.shape(a)[-1]])
  if not tf.executing_eagerly():
    ret.set_shape([None] + a.get_shape().as_list()[-1:])
  return ret