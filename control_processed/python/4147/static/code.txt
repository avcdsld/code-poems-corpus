def train(hparams, output_dir, env_problem_name, report_fn=None):
  """Train."""
  env_fn = initialize_env_specs(hparams, env_problem_name)

  tf.logging.vlog(1, "HParams in trainer_model_free.train : %s",
                  misc_utils.pprint_hparams(hparams))
  tf.logging.vlog(1, "Using hparams.base_algo: %s", hparams.base_algo)
  learner = rl_utils.LEARNERS[hparams.base_algo](
      hparams.frame_stack_size, output_dir, output_dir, total_num_epochs=1
  )

  policy_hparams = trainer_lib.create_hparams(hparams.base_algo_params)
  rl_utils.update_hparams_from_hparams(
      policy_hparams, hparams, hparams.base_algo + "_"
  )

  tf.logging.vlog(1, "Policy HParams : %s",
                  misc_utils.pprint_hparams(policy_hparams))

  # TODO(konradczechowski): remove base_algo dependance, when evaluation method
  # will be decided
  if hparams.base_algo == "ppo":
    total_steps = policy_hparams.epochs_num
    tf.logging.vlog(2, "total_steps: %d", total_steps)

    eval_every_epochs = policy_hparams.eval_every_epochs
    tf.logging.vlog(2, "eval_every_epochs: %d", eval_every_epochs)

    if eval_every_epochs == 0:
      eval_every_epochs = total_steps
    policy_hparams.eval_every_epochs = 0

    metric_name = rl_utils.get_metric_name(
        sampling_temp=hparams.eval_sampling_temps[0],
        max_num_noops=hparams.eval_max_num_noops,
        clipped=False
    )

    tf.logging.vlog(1, "metric_name: %s", metric_name)

    eval_metrics_dir = os.path.join(output_dir, "eval_metrics")
    eval_metrics_dir = os.path.expanduser(eval_metrics_dir)
    tf.gfile.MakeDirs(eval_metrics_dir)
    eval_metrics_writer = tf.summary.FileWriter(eval_metrics_dir)

    def evaluate_on_new_model(model_dir_path):
      global step
      eval_metrics = rl_utils.evaluate_all_configs(hparams, model_dir_path)
      tf.logging.info(
          "Agent eval metrics:\n{}".format(pprint.pformat(eval_metrics)))
      rl_utils.summarize_metrics(eval_metrics_writer, eval_metrics, step)
      if report_fn:
        report_fn(eval_metrics[metric_name], step)
      step += 1

    policy_hparams.epochs_num = total_steps
    policy_hparams.save_models_every_epochs = eval_every_epochs
  else:
    def evaluate_on_new_model(model_dir_path):
      del model_dir_path
      raise NotImplementedError(
          "This function is currently implemented only for ppo")

  learner.train(env_fn,
                policy_hparams,
                simulated=False,
                save_continuously=True,
                epoch=0,
                model_save_fn=evaluate_on_new_model)