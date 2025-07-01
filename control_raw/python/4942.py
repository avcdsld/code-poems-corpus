def setup_env(hparams,
              batch_size,
              max_num_noops,
              rl_env_max_episode_steps=-1,
              env_name=None):
  """Setup."""
  if not env_name:
    env_name = full_game_name(hparams.game)

  maxskip_envs = should_apply_max_and_skip_env(hparams)

  env = T2TGymEnv(
      base_env_name=env_name,
      batch_size=batch_size,
      grayscale=hparams.grayscale,
      should_derive_observation_space=hparams
      .rl_should_derive_observation_space,
      resize_width_factor=hparams.resize_width_factor,
      resize_height_factor=hparams.resize_height_factor,
      rl_env_max_episode_steps=rl_env_max_episode_steps,
      max_num_noops=max_num_noops,
      maxskip_envs=maxskip_envs,
      sticky_actions=hparams.sticky_actions
  )
  return env