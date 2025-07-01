def get_latent_pred_loss(latents_pred, latents_discrete_hot, hparams):
  """Latent prediction and loss."""
  latents_logits = tf.layers.dense(
      latents_pred, 2**hparams.bottleneck_bits, name="extra_logits")
  loss = tf.nn.softmax_cross_entropy_with_logits_v2(
      labels=tf.stop_gradient(latents_discrete_hot), logits=latents_logits)
  return loss