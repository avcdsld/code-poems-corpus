def _curvature_range(self):
    """Curvature range.

    Returns:
      h_max_t, h_min_t ops
    """
    self._curv_win = tf.get_variable("curv_win",
                                     dtype=tf.float32,
                                     trainable=False,
                                     shape=[self.curvature_window_width,],
                                     initializer=tf.zeros_initializer)
    # We use log smoothing for curvature range
    self._curv_win = tf.scatter_update(self._curv_win,
                                       self._step % self.curvature_window_width,
                                       tf.log(self._grad_norm_squared))
    # Note here the iterations start from iteration 0
    valid_window = tf.slice(self._curv_win,
                            tf.constant([0,]),
                            tf.expand_dims(
                                tf.minimum(
                                    tf.constant(self.curvature_window_width),
                                    self._step + 1), dim=0))
    self._h_min_t = tf.reduce_min(valid_window)
    self._h_max_t = tf.reduce_max(valid_window)

    curv_range_ops = []
    with tf.control_dependencies([self._h_min_t, self._h_max_t]):
      avg_op = self._moving_averager.apply([self._h_min_t, self._h_max_t])
      with tf.control_dependencies([avg_op]):
        self._h_min = tf.exp(
            tf.identity(self._moving_averager.average(self._h_min_t)))
        self._h_max = tf.exp(
            tf.identity(self._moving_averager.average(self._h_max_t)))
        if self._sparsity_debias:
          self._h_min *= self._sparsity_avg
          self._h_max *= self._sparsity_avg
    curv_range_ops.append(avg_op)
    return curv_range_ops