def raw_nogpu_session(graph=None):
  """tf.Session, hiding GPUs."""
  config = tf.compat.v1.ConfigProto(device_count={'GPU': 0})
  return tf.compat.v1.Session(config=config, graph=graph)