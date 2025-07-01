def autoencoder_discrete_tiny():
  """Discrete autoencoder model for compressing pong frames for testing."""
  hparams = autoencoder_ordered_discrete()
  hparams.num_hidden_layers = 2
  hparams.bottleneck_bits = 24
  hparams.batch_size = 2
  hparams.gan_loss_factor = 0.
  hparams.bottleneck_l2_factor = 0.001
  hparams.add_hparam("video_modality_loss_cutoff", 0.02)
  hparams.num_residual_layers = 1
  hparams.hidden_size = 32
  hparams.max_hidden_size = 64
  return hparams