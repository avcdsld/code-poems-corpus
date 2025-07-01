def conv_block(name, x, mid_channels, dilations=None, activation="relu",
               dropout=0.0):
  """2 layer conv block used in the affine coupling layer.

  Args:
    name: variable scope.
    x: 4-D or 5-D Tensor.
    mid_channels: Output channels of the second layer.
    dilations: Optional, list of integers.
    activation: relu or gatu.
      If relu, the second layer is relu(W*x)
      If gatu, the second layer is tanh(W1*x) * sigmoid(W2*x)
    dropout: Dropout probability.
  Returns:
    x: 4-D Tensor: Output activations.
  """
  with tf.variable_scope(name, reuse=tf.AUTO_REUSE):

    x_shape = common_layers.shape_list(x)
    is_2d = len(x_shape) == 4
    num_steps = x_shape[1]
    if is_2d:
      first_filter = [3, 3]
      second_filter = [1, 1]
    else:
      # special case when number of steps equal 1 to avoid
      # padding.
      if num_steps == 1:
        first_filter = [1, 3, 3]
      else:
        first_filter = [2, 3, 3]
      second_filter = [1, 1, 1]

    # Edge Padding + conv2d + actnorm + relu:
    # [output: 512 channels]
    x = conv("1_1", x, output_channels=mid_channels, filter_size=first_filter,
             dilations=dilations)
    x = tf.nn.relu(x)
    x = get_dropout(x, rate=dropout)

    # Padding + conv2d + actnorm + activation.
    # [input, output: 512 channels]
    if activation == "relu":
      x = conv("1_2", x, output_channels=mid_channels,
               filter_size=second_filter, dilations=dilations)
      x = tf.nn.relu(x)
    elif activation == "gatu":
      # x = tanh(w1*x) * sigm(w2*x)
      x_tanh = conv("1_tanh", x, output_channels=mid_channels,
                    filter_size=second_filter, dilations=dilations)
      x_sigm = conv("1_sigm", x, output_channels=mid_channels,
                    filter_size=second_filter, dilations=dilations)
      x = tf.nn.tanh(x_tanh) * tf.nn.sigmoid(x_sigm)

    x = get_dropout(x, rate=dropout)
    return x