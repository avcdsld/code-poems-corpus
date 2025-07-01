def setup_and_load_epoch(hparams, data_dir, which_epoch_data=None):
  """Load T2TGymEnv with data from one epoch.

  Args:
    hparams: hparams.
    data_dir: data directory.
    which_epoch_data: data from which epoch to load.

  Returns:
    env.
  """
  t2t_env = rl_utils.setup_env(
      hparams, batch_size=hparams.real_batch_size,
      max_num_noops=hparams.max_num_noops
  )
  # Load data.
  if which_epoch_data is not None:
    if which_epoch_data == "last":
      which_epoch_data = infer_last_epoch_num(data_dir)
    assert isinstance(which_epoch_data, int), \
      "{}".format(type(which_epoch_data))
    t2t_env.start_new_epoch(which_epoch_data, data_dir)
  else:
    t2t_env.start_new_epoch(-999)
  return t2t_env