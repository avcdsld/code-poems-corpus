def _grad_sparsity(self):
    """Gradient sparsity."""
    # If the sparse minibatch gradient has 10 percent of its entries
    # non-zero, its sparsity is 0.1.
    # The norm of dense gradient averaged from full dataset
    # are roughly estimated norm of minibatch
    # sparse gradient norm * sqrt(sparsity)
    # An extension maybe only correct the sparse blob.
    non_zero_cnt = tf.add_n([tf.count_nonzero(g) for g in self._grad])
    all_entry_cnt = tf.add_n([tf.size(g) for g in self._grad])
    self._sparsity = tf.cast(non_zero_cnt, self._grad[0].dtype)
    self._sparsity /= tf.cast(all_entry_cnt, self._grad[0].dtype)
    avg_op = self._moving_averager.apply([self._sparsity,])
    with tf.control_dependencies([avg_op]):
      self._sparsity_avg = self._moving_averager.average(self._sparsity)
    return avg_op