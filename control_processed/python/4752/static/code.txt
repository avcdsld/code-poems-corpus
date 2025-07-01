def next_frame_savp_gan():
  """SAVP - GAN only model."""
  hparams = next_frame_savp()
  hparams.use_gan = True
  hparams.use_vae = False
  hparams.gan_loss_multiplier = 0.001
  hparams.optimizer_adam_beta1 = 0.5
  hparams.learning_rate_constant = 2e-4
  hparams.gan_loss = "cross_entropy"
  hparams.learning_rate_decay_steps = 100000
  hparams.learning_rate_schedule = "constant*linear_decay"
  return hparams