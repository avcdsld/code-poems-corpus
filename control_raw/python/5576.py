def bottleneck_block(inputs,
                     filters,
                     is_training,
                     projection_shortcut,
                     strides,
                     final_block,
                     data_format="channels_first",
                     use_td=False,
                     targeting_rate=None,
                     keep_prob=None):
  """Bottleneck block variant for residual networks with BN after convolutions.

  Args:
    inputs: `Tensor` of size `[batch, channels, height, width]`.
    filters: `int` number of filters for the first two convolutions. Note that
        the third and final convolution will use 4 times as many filters.
    is_training: `bool` for whether the model is in training.
    projection_shortcut: `function` to use for projection shortcuts (typically
        a 1x1 convolution to match the filter dimensions). If None, no
        projection is used and the input is passed as unchanged through the
        shortcut connection.
    strides: `int` block stride. If greater than 1, this block will ultimately
        downsample the input.
    final_block: `bool` set to True if it is this the final block in the group.
        This is changes the behavior of batch normalization initialization for
        the final batch norm in a block.
    data_format: `str` either "channels_first" for `[batch, channels, height,
        width]` or "channels_last for `[batch, height, width, channels]`.
    use_td: `str` one of "weight" or "unit". Set to False or "" to disable
      targeted dropout.
    targeting_rate: `float` proportion of weights to target with targeted
      dropout.
    keep_prob: `float` keep probability for targeted dropout.

  Returns:
    The output `Tensor` of the block.
  """
  # TODO(chrisying): this block is technically the post-activation resnet-v1
  # bottleneck unit. Test with v2 (pre-activation) and replace if there is no
  # difference for consistency.
  shortcut = inputs
  if projection_shortcut is not None:
    shortcut = projection_shortcut(inputs)

  inputs = conv2d_fixed_padding(
      inputs=inputs,
      filters=filters,
      kernel_size=1,
      strides=1,
      data_format=data_format,
      use_td=use_td,
      targeting_rate=targeting_rate,
      keep_prob=keep_prob,
      is_training=is_training)

  inputs = batch_norm_relu(inputs, is_training, data_format=data_format)
  inputs = conv2d_fixed_padding(
      inputs=inputs,
      filters=filters,
      kernel_size=3,
      strides=strides,
      data_format=data_format,
      use_td=use_td,
      targeting_rate=targeting_rate,
      keep_prob=keep_prob,
      is_training=is_training)

  inputs = batch_norm_relu(inputs, is_training, data_format=data_format)
  inputs = conv2d_fixed_padding(
      inputs=inputs,
      filters=4 * filters,
      kernel_size=1,
      strides=1,
      data_format=data_format,
      use_td=use_td,
      targeting_rate=targeting_rate,
      keep_prob=keep_prob,
      is_training=is_training)
  inputs = batch_norm_relu(
      inputs,
      is_training,
      relu=False,
      init_zero=final_block,
      data_format=data_format)

  return tf.nn.relu(inputs + shortcut)