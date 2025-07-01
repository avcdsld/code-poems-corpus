def belu(x):
  """Bipolar ELU as in https://arxiv.org/abs/1709.04054."""
  x_shape = shape_list(x)
  x1, x2 = tf.split(tf.reshape(x, x_shape[:-1] + [-1, 2]), 2, axis=-1)
  y1 = tf.nn.elu(x1)
  y2 = -tf.nn.elu(-x2)
  return tf.reshape(tf.concat([y1, y2], axis=-1), x_shape)