def ppo_original_world_model_stochastic_discrete():
  """Atari parameters with stochastic discrete world model as policy."""
  hparams = ppo_original_params()
  hparams.policy_network = "next_frame_basic_stochastic_discrete"
  hparams_keys = hparams.values().keys()
  video_hparams = basic_stochastic.next_frame_basic_stochastic_discrete()
  for (name, value) in six.iteritems(video_hparams.values()):
    if name in hparams_keys:
      hparams.set_hparam(name, value)
    else:
      hparams.add_hparam(name, value)
  # To avoid OOM. Probably way to small.
  hparams.optimization_batch_size = 1
  hparams.weight_decay = 0
  return hparams