def decompress_step(source, hparams, first_relu, name):
  """Decompression function."""
  with tf.variable_scope(name):
    shape = common_layers.shape_list(source)
    multiplier = 2
    kernel = (1, 1)
    thicker = common_layers.conv_block(
        source,
        hparams.hidden_size * multiplier, [((1, 1), kernel)],
        first_relu=first_relu,
        name="decompress_conv")
    return tf.reshape(thicker, [shape[0], shape[1] * 2, 1, hparams.hidden_size])