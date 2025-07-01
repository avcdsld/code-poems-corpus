def generate_data_for_env_problem(problem_name):
  """Generate data for `EnvProblem`s."""
  assert FLAGS.env_problem_max_env_steps > 0, ("--env_problem_max_env_steps "
                                               "should be greater than zero")
  assert FLAGS.env_problem_batch_size > 0, ("--env_problem_batch_size should be"
                                            " greather than zero")
  problem = registry.env_problem(problem_name)
  task_id = None if FLAGS.task_id < 0 else FLAGS.task_id
  data_dir = os.path.expanduser(FLAGS.data_dir)
  tmp_dir = os.path.expanduser(FLAGS.tmp_dir)
  # TODO(msaffar): Handle large values for env_problem_batch_size where we
  #  cannot create that many environments within the same process.
  problem.initialize(batch_size=FLAGS.env_problem_batch_size)
  env_problem_utils.play_env_problem_randomly(
      problem, num_steps=FLAGS.env_problem_max_env_steps)
  problem.generate_data(data_dir=data_dir, tmp_dir=tmp_dir, task_id=task_id)