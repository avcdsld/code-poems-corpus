def aggregate_task_lm_losses(hparams,
                             problem_hparams,
                             logits,
                             feature_name,
                             feature):
  """LM loss for multiproblems."""
  summaries = []
  vocab_size = problem_hparams.vocab_size[feature_name]
  if vocab_size is not None and hasattr(hparams, "vocab_divisor"):
    vocab_size += (-vocab_size) % hparams.vocab_divisor
  modality = problem_hparams.modality[feature_name]
  loss = hparams.loss.get(feature_name, modalities.get_loss(modality))
  weights_fn = hparams.weights_fn.get(
      feature_name, modalities.get_weights_fn(modality))
  loss_num = 0.
  loss_den = 0.
  for task in hparams.problem.task_list:
    loss_num_, loss_den_ = loss(
        logits, feature,
        lambda x: common_layers.weights_multi_problem_all(x, task.task_id),  # pylint: disable=cell-var-from-loop
        hparams, vocab_size, weights_fn)

    loss_num += loss_num_
    loss_den += loss_den_

    loss_val = loss_num_ / tf.maximum(1.0, loss_den_)
    summaries.append([task.name+"_loss", loss_val])

  return loss_num, loss_den, summaries