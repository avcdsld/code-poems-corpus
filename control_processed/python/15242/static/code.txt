def run_one_step(self, eig_init_vec_val, eig_num_iter_val, smooth_val,
                   penalty_val, learning_rate_val):
    """Run one step of gradient descent for optimization.

    Args:
      eig_init_vec_val: Start value for eigen value computations
      eig_num_iter_val: Number of iterations to run for eigen computations
      smooth_val: Value of smoothness parameter
      penalty_val: Value of penalty for the current step
      learning_rate_val: Value of learning rate
    Returns:
     found_cert: True is negative certificate is found, False otherwise
    """
    # Running step
    step_feed_dict = {self.eig_init_vec_placeholder: eig_init_vec_val,
                      self.eig_num_iter_placeholder: eig_num_iter_val,
                      self.smooth_placeholder: smooth_val,
                      self.penalty_placeholder: penalty_val,
                      self.learning_rate: learning_rate_val}

    if self.params['eig_type'] == 'SCIPY':
      current_eig_vector, self.current_eig_val_estimate = self.get_scipy_eig_vec()
      step_feed_dict.update({
          self.eig_vec_estimate: current_eig_vector
      })
    elif self.params['eig_type'] == 'LZS':
      step_feed_dict.update({
          self.dual_object.m_min_vec_ph: self.dual_object.m_min_vec_estimate
      })

    self.sess.run(self.train_step, feed_dict=step_feed_dict)

    [
        _, self.dual_object.m_min_vec_estimate, self.current_eig_val_estimate
    ] = self.sess.run([
        self.proj_step,
        self.eig_vec_estimate,
        self.eig_val_estimate
    ], feed_dict=step_feed_dict)

    if self.current_step % self.params['print_stats_steps'] == 0:
      [self.current_total_objective, self.current_unconstrained_objective,
       self.dual_object.m_min_vec_estimate,
       self.current_eig_val_estimate,
       self.current_nu] = self.sess.run(
           [self.total_objective,
            self.dual_object.unconstrained_objective,
            self.eig_vec_estimate,
            self.eig_val_estimate,
            self.dual_object.nu], feed_dict=step_feed_dict)

      stats = {
          'total_objective':
              float(self.current_total_objective),
          'unconstrained_objective':
              float(self.current_unconstrained_objective),
          'min_eig_val_estimate':
              float(self.current_eig_val_estimate)
      }
      tf.logging.info('Current inner step: %d, optimization stats: %s',
                      self.current_step, stats)
      if self.params['stats_folder'] is not None:
        stats = json.dumps(stats)
        filename = os.path.join(self.params['stats_folder'],
                                str(self.current_step) + '.json')
        with tf.gfile.Open(filename) as file_f:
          file_f.write(stats)

    # Project onto feasible set of dual variables
    if self.current_step % self.params['projection_steps'] == 0 and self.current_unconstrained_objective < 0:
      nu = self.sess.run(self.dual_object.nu)
      dual_feed_dict = {
          self.dual_object.h_min_vec_ph: self.dual_object.h_min_vec_estimate
      }
      _, min_eig_val_h_lz = self.dual_object.get_lanczos_eig(compute_m=False, feed_dict=dual_feed_dict)
      projected_dual_feed_dict = {
          self.dual_object.projected_dual.nu: nu,
          self.dual_object.projected_dual.min_eig_val_h: min_eig_val_h_lz
      }
      if self.dual_object.projected_dual.compute_certificate(self.current_step, projected_dual_feed_dict):
        return True

    return False