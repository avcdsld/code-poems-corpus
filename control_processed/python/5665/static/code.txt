def decompress_decoder_1d(x, hparams, name=None):
  """Decoder that decompresses 1-D inputs by 2**num_compress_steps.

  Args:
    x: Tensor of shape [batch, compress_length, channels].
    hparams: HParams.
    name: string, variable scope.

  Returns:
    Tensor of shape [batch, length, hparams.hidden_size].
  """
  x = tf.expand_dims(x, axis=2)
  output = decompress_decoder(x, hparams,
                              strides=(2, 1),
                              kernel=(hparams.kernel_size, 1),
                              name=name)
  return tf.squeeze(output, axis=2)