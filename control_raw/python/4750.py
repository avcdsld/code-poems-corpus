def next_frame_savp():
  """SAVP model hparams."""
  hparams = sv2p_params.next_frame_sv2p()
  hparams.add_hparam("z_dim", 8)
  hparams.add_hparam("num_discriminator_filters", 32)
  hparams.add_hparam("use_vae", True)
  hparams.add_hparam("use_gan", False)
  hparams.add_hparam("use_spectral_norm", True)
  hparams.add_hparam("gan_loss", "cross_entropy")
  hparams.add_hparam("gan_loss_multiplier", 0.01)
  hparams.add_hparam("gan_vae_loss_multiplier", 0.01)
  hparams.add_hparam("gan_optimization", "joint")
  hparams.bottom = {
      "inputs": modalities.video_raw_bottom,
      "targets": modalities.video_raw_targets_bottom,
  }
  hparams.loss = {
      "targets": modalities.video_l1_raw_loss,
  }
  hparams.top = {
      "targets": modalities.video_raw_top,
  }
  hparams.latent_loss_multiplier_schedule = "linear"
  hparams.upsample_method = "bilinear_upsample_conv"
  hparams.internal_loss = False
  hparams.reward_prediction = False
  hparams.anneal_end = 100000
  hparams.num_iterations_1st_stage = 0
  hparams.num_iterations_2nd_stage = 50000
  return hparams