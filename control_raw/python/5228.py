def encoder_decoder_attention_loss(expected_attention_logits,
                                   actual_attentions,
                                   loss_type="kl_divergence",
                                   loss_multiplier=1.0):
  """Computes encdec attention loss between expected and actual attentions.

  Args:
    expected_attention_logits: Tensor storing the expected encoder-decoder
      attention logits with shape [batch_size, target_length, input_length].
    actual_attentions: Dictionary with actual attention logits for different
      attention types and hidden layers.
    loss_type: type of the loss function.
    loss_multiplier: multiplier for the attention loss.

  Returns:
    KL_divergence loss between the actual and expected attention logits.
  """

  def combine_attentions(attention_list):
    """Combine different layer attentions and then average over layers/heads."""
    # Stack all hidden layer attention tensors to get a tensor with shape
    # [num_hidden_layers, batch_size, num_heads, target_length, input_length].
    attentions = tf.stack(attention_list)
    # Reduce mean across all layers (axis=0) and all heads (axis=2) to get a
    # tensor with shape [batch_size, target_length, input_length].
    return tf.reduce_mean(attentions, [0, 2])

  def kl_divergence_loss(expected_logits, actual_logits):
    p = tfp.distributions.Categorical(logits=expected_logits)
    q = tfp.distributions.Categorical(logits=actual_logits)
    return tfp.distributions.kl_divergence(p, q)

  def mse_loss(expected_logits, actual_weights):
    expected_weights = tf.nn.softmax(expected_logits)
    return tf.losses.mean_squared_error(expected_weights, actual_weights)

  # For each hidden layer, we have attention-logit and attention-weight tensors
  # with shape [batch_size, num_heads, target_length, input_length].
  loss = 0.0
  if loss_type == "mse":
    actual_encdec_attention_weights = [
        t for layer_key, t in actual_attentions.items()
        if "encdec_attention" in layer_key and not layer_key.endswith("/logits")
    ]
    actual_attention_weights = combine_attentions(
        actual_encdec_attention_weights)
    loss = mse_loss(expected_attention_logits, actual_attention_weights)
  else:
    actual_encdec_attention_logits = [
        t for layer_key, t in actual_attentions.items()
        if "encdec_attention" in layer_key and layer_key.endswith("/logits")
    ]
    actual_attention_logits = combine_attentions(actual_encdec_attention_logits)
    loss = kl_divergence_loss(expected_attention_logits,
                              actual_attention_logits)
  return loss * loss_multiplier