def maybe_reshape_4d_to_3d(x):
  """Reshape input from 4D to 3D if necessary."""
  x_shape = common_layers.shape_list(x)
  is_4d = False
  if len(x_shape) == 4:
    x = tf.reshape(x, [x_shape[0], x_shape[1]*x_shape[2], x_shape[3]])
    is_4d = True
  return x, x_shape, is_4d