def downsample_residual(x, output_channels, dim='2d', stride=1, scope='h'):
  """Downsamples 'x' by `stride` using average pooling.

  Args:
    x: input tensor of size [N, H, W, C]
    output_channels: Desired number of output channels.
    dim: '2d' if 2-dimensional, '3d' if 3-dimensional.
    stride: What stride to use. Usually 1 or 2.
    scope: Optional variable scope.

  Returns:
    A downsampled tensor of size [N, H/2, W/2, output_channels] if stride
    is 2, else returns a tensor of size [N, H, W, output_channels] if
    stride is 1.
  """
  with tf.variable_scope(scope):
    if stride > 1:
      avg_pool = CONFIG[dim]['avg_pool']
      x = avg_pool(x,
                   pool_size=(stride, stride),
                   strides=(stride, stride),
                   padding='VALID')

    input_channels = tf.shape(x)[3]
    diff = output_channels - input_channels
    x = tf.pad(
        x, [[0, 0], [0, 0], [0, 0],
            [diff // 2, diff // 2]])
    return x