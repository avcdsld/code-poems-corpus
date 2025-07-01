def rlmb_ppo_base():
  """HParams for PPO base."""
  hparams = _rlmb_base()
  ppo_params = dict(
      base_algo="ppo",
      base_algo_params="ppo_original_params",
      # Number of real environments to train on simultaneously.
      real_batch_size=1,
      # Number of simulated environments to train on simultaneously.
      simulated_batch_size=16,
      eval_batch_size=32,

      # Unused; number of PPO epochs is calculated from the real frame limit.
      real_ppo_epochs_num=0,
      # Number of frames that can be taken from the simulated environment before
      # it diverges, used for training the agent.

      ppo_epochs_num=1000,  # This should be enough to see something
      # Should be equal to simulated_rollout_length.
      # TODO(koz4k): Uncouple this by outputing done from SimulatedBatchEnv.
      ppo_epoch_length=hparams.simulated_rollout_length,
      # Do not eval since simulated batch env does not produce dones
      ppo_eval_every_epochs=0,
      ppo_learning_rate_constant=1e-4,  # Will be changed, just so it exists.
      # This needs to be divisible by real_ppo_effective_num_agents.
      real_ppo_epoch_length=16 * 200,
      real_ppo_learning_rate_constant=1e-4,
      real_ppo_effective_num_agents=16,
      real_ppo_eval_every_epochs=0,

      simulation_flip_first_random_for_beginning=True,
  )
  update_hparams(hparams, ppo_params)
  return hparams