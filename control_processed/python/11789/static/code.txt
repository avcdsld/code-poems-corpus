def channel(layer, n_channel, batch=None):
  """Visualize a single channel"""
  if batch is None:
    return lambda T: tf.reduce_mean(T(layer)[..., n_channel])
  else:
    return lambda T: tf.reduce_mean(T(layer)[batch, ..., n_channel])