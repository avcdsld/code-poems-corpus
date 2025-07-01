def run_all(logdir, steps, thresholds, verbose=False):
  """Generate PR curve summaries.

  Arguments:
    logdir: The directory into which to store all the runs' data.
    steps: The number of steps to run for.
    verbose: Whether to print the names of runs into stdout during execution.
    thresholds: The number of thresholds to use for PR curves.
  """
  # First, we generate data for a PR curve that assigns even weights for
  # predictions of all classes.
  run_name = 'colors'
  if verbose:
    print('--- Running: %s' % run_name)
  start_runs(
      logdir=logdir,
      steps=steps,
      run_name=run_name,
      thresholds=thresholds)

  # Next, we generate data for a PR curve that assigns arbitrary weights to
  # predictions.
  run_name = 'mask_every_other_prediction'
  if verbose:
    print('--- Running: %s' % run_name)
  start_runs(
      logdir=logdir,
      steps=steps,
      run_name=run_name,
      thresholds=thresholds,
      mask_every_other_prediction=True)