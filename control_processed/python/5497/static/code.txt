def roc_auc(logits, labels, weights_fn=None):
  """Calculate ROC AUC.

  Requires binary classes.

  Args:
    logits: Tensor of size [batch_size, 1, 1, num_classes]
    labels: Tensor of size [batch_size, 1, 1, num_classes]
    weights_fn: Function that takes in labels and weighs examples (unused)
  Returns:
    ROC AUC (scalar), weights
  """
  del weights_fn
  with tf.variable_scope("roc_auc", values=[logits, labels]):
    predictions = tf.argmax(logits, axis=-1)
    _, auc = tf.metrics.auc(labels, predictions, curve="ROC")
    return auc, tf.constant(1.0)