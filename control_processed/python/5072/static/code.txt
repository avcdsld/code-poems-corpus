def image_top(body_output, targets, model_hparams, vocab_size):
  """Top transformation for images."""
  del targets  # unused arg
  # TODO(lukaszkaiser): is this a universal enough way to get channels?
  num_channels = model_hparams.problem.num_channels
  with tf.variable_scope("rgb_softmax"):
    body_output_shape = common_layers.shape_list(body_output)
    reshape_shape = body_output_shape[:3]
    reshape_shape.extend([num_channels, vocab_size])
    res = tf.layers.dense(body_output, vocab_size * num_channels)
    res = tf.reshape(res, reshape_shape)
    if not tf.get_variable_scope().reuse:
      res_argmax = tf.argmax(res, axis=-1)
      tf.summary.image(
          "result",
          common_layers.tpu_safe_image_summary(res_argmax),
          max_outputs=1)
    return res