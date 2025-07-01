def aggregate_task_losses(hparams,
                          problem_hparams,
                          logits,
                          feature_name,
                          feature):
  """Multiproblem loss function."""

  # If no reweighting, we want the default loss to mimic the LM loss.
  if not hparams.multiproblem_reweight_label_loss:
    return aggregate_task_lm_losses(hparams=hparams,
                                    problem_hparams=problem_hparams,
                                    logits=logits,
                                    feature_name=feature_name,
                                    feature=feature)

  summaries = []
  main_task_id = hparams.problem.task_list[0].task_id
  vocab_size = problem_hparams.vocab_size[feature_name]
  if vocab_size is not None and hasattr(hparams, "vocab_divisor"):
    vocab_size += (-vocab_size) % hparams.vocab_divisor
  modality = problem_hparams.modality[feature_name]
  loss = hparams.loss.get(feature_name, modalities.get_loss(modality))
  weights_fn = hparams.weights_fn.get(
      feature_name, modalities.get_weights_fn(modality))
  # Primary task loss
  loss_num, loss_den = loss(
      logits, feature,
      lambda x: common_layers.weights_multi_problem_all(x, main_task_id),
      hparams, vocab_size, weights_fn)

  loss_val = loss_num / tf.maximum(1.0, loss_den)
  summaries.append([hparams.problem.task_list[0].name+"_loss", loss_val])

  # Since the losses may undergo rescaling, they cannot exist as separate
  # numerators and denominators. Set the denominators to 1 in order to faciliate
  # loss averaging.
  loss_num = loss_val
  loss_den = tf.minimum(tf.convert_to_tensor(1, dtype=tf.float32), loss_den)

  for task in hparams.problem.task_list[1:]:
    # Loss only from the input sequence -- the auxiliary LM loss.
    seq_loss_num, seq_loss_den = loss(
        logits, feature,
        lambda x: common_layers.weights_multi_problem_input(x, task.task_id),  # pylint: disable=cell-var-from-loop
        hparams, vocab_size)
    seq_loss_num *= problem_hparams.loss_multiplier

    # Unscaled sequence loss.
    seq_loss = seq_loss_num / tf.maximum(1.0, seq_loss_den)
    summaries.append([task.name+"_seq_loss", seq_loss])

    if hasattr(task, "num_classes"):
      # Loss only from the classification label.
      label_loss_num, label_loss_den = loss(
          logits, feature,
          lambda x: common_layers.weights_multi_problem(x, task.task_id),  # pylint: disable=cell-var-from-loop
          hparams, vocab_size)
      label_loss_num *= problem_hparams.loss_multiplier

      # Unscaled classification label loss.
      label_loss = label_loss_num / tf.maximum(1.0, label_loss_den)
      summaries.append([task.name+"_label_loss", label_loss])

      # Scaling.
      if hparams.multiproblem_reweight_label_loss:
        label_loss *= hparams.multiproblem_label_weight
        seq_loss *= (1 - hparams.multiproblem_label_weight)

      # This is the training loss for the optimizer after scaling.
      task_loss_val = seq_loss + label_loss

      loss_den_ = label_loss_den

    else:
      # Loss only from the target sequence.
      target_loss_num, target_loss_den = loss(
          logits, feature,
          lambda x: common_layers.weights_multi_problem(x, task.task_id),  # pylint: disable=cell-var-from-loop
          hparams, vocab_size)
      target_loss_num *= problem_hparams.loss_multiplier

      # Unscaled target sequence loss.
      target_loss = target_loss_num / tf.maximum(1.0, target_loss_den)
      summaries.append([task.name+"_target_loss", target_loss])

      # Scaling.
      if hparams.multiproblem_reweight_label_loss:
        target_loss *= hparams.multiproblem_label_weight
        seq_loss *= (1 - hparams.multiproblem_label_weight)

      # This is the training loss for the optimizer after all the scaling.
      task_loss_val = seq_loss + target_loss

      loss_den_ = target_loss_den

    summaries.append([task.name+"_loss", task_loss_val])
    # Adding 1 to the loss den for each task leads to averaging task losses.
    # TODO(urvashik): Fix combination with other task losses - weighted
    # average based on the number of examples from that task.
    loss_num += task_loss_val
    loss_den += tf.minimum(tf.convert_to_tensor(1, dtype=tf.float32),
                           loss_den_)

  return loss_num, loss_den, summaries