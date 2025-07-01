def class_label_top(body_output, targets, model_hparams, vocab_size):
  """Transform inputs from model space to target space.

  Average over inner dims and a linear layer to logits.

  Args:
    body_output: A Tensor with shape [batch, ?, ?, body_output_size].
    targets:
    model_hparams: HParams, model hyperparmeters.
    vocab_size: int, vocabulary size.

  Returns:
    a Tensors, each with shape [batch_size, 1, 1, 1, vocab_size]
  """
  del targets  # unused arg
  with tf.variable_scope("class_label_modality_%d_%d" % (
      vocab_size, model_hparams.hidden_size)):
    x = body_output
    x = tf.reduce_mean(x, axis=[1, 2], keepdims=True)
    res = tf.layers.dense(x, vocab_size)
    return tf.expand_dims(res, 3)