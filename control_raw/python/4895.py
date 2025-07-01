def reshape_like_all_dims(a, b):
  """Reshapes a to match the shape of b."""
  ret = tf.reshape(a, tf.shape(b))
  if not tf.executing_eagerly():
    ret.set_shape(b.get_shape())
  return ret