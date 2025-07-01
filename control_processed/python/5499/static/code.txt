def create_eager_metrics_for_problem(problem, model_hparams):
  """See create_eager_metrics."""
  metric_fns = problem.eval_metric_fns(model_hparams)
  problem_hparams = problem.get_hparams(model_hparams)
  target_modality = problem_hparams.modality["targets"]
  weights_fn = model_hparams.weights_fn.get(
      "targets",
      modalities.get_weights_fn(target_modality))
  return create_eager_metrics_internal(metric_fns, weights_fn=weights_fn)