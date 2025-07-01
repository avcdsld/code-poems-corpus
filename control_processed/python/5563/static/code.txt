def autoencoder_range(rhp):
  """Tuning grid of the main autoencoder params."""
  rhp.set_float("dropout", 0.01, 0.3)
  rhp.set_float("gan_loss_factor", 0.01, 0.1)
  rhp.set_float("bottleneck_l2_factor", 0.001, 0.1, scale=rhp.LOG_SCALE)
  rhp.set_discrete("bottleneck_warmup_steps", [200, 2000])
  rhp.set_float("gumbel_temperature", 0, 1)
  rhp.set_float("gumbel_noise_factor", 0, 0.5)