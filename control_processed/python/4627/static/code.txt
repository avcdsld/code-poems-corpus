def evaluate_train_and_eval(step, inputs, predict_fun, eval_steps, rng,
                            train_sw=None, eval_sw=None, history=None):
  """Evalaute on train and eval data, and log metrics."""
  step_log(step, "Evaluation")
  train_metrics, eval_metrics = [
      evaluate(  # pylint: disable=g-complex-comprehension
          itertools.islice(input_stream(), eval_steps),
          predict_fun,
          _METRICS,
          rng)
      for input_stream in
      [inputs.train_eval_stream, inputs.eval_stream]]
  if train_sw:
    log_metrics(train_metrics, train_sw, "train", step, history=history)
  if eval_sw:
    log_metrics(eval_metrics, eval_sw, "eval", step, history=history)
  step_log(step, "Finished evaluation")
  return train_metrics, eval_metrics