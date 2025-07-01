def image_channel_embeddings_top(body_output,
                                 targets,
                                 model_hparams,
                                 vocab_size):
  """Top transformation for images."""
  del targets  # unused arg
  with tf.variable_scope("image_channel_embeddings_bottom"):
    img_len = model_hparams.img_len
    channels = model_hparams.num_channels
    x = tf.layers.dense(
        body_output, 256, use_bias=True, activation=None, name="output_conv")
    x = tf.reshape(x,
                   [-1, img_len, img_len, channels, vocab_size])
    return x