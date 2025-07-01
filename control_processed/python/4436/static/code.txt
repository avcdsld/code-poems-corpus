def _get_cubic_root(self):
    """Get the cubic root."""
    # We have the equation x^2 D^2 + (1-x)^4 * C / h_min^2
    # where x = sqrt(mu).
    # We substitute x, which is sqrt(mu), with x = y + 1.
    # It gives y^3 + py = q
    # where p = (D^2 h_min^2)/(2*C) and q = -p.
    # We use the Vieta's substitution to compute the root.
    # There is only one real solution y (which is in [0, 1] ).
    # http://mathworld.wolfram.com/VietasSubstitution.html
    assert_array = [
        tf.Assert(
            tf.logical_not(tf.is_nan(self._dist_to_opt_avg)),
            [self._dist_to_opt_avg,]),
        tf.Assert(
            tf.logical_not(tf.is_nan(self._h_min)),
            [self._h_min,]),
        tf.Assert(
            tf.logical_not(tf.is_nan(self._grad_var)),
            [self._grad_var,]),
        tf.Assert(
            tf.logical_not(tf.is_inf(self._dist_to_opt_avg)),
            [self._dist_to_opt_avg,]),
        tf.Assert(
            tf.logical_not(tf.is_inf(self._h_min)),
            [self._h_min,]),
        tf.Assert(
            tf.logical_not(tf.is_inf(self._grad_var)),
            [self._grad_var,])
    ]
    with tf.control_dependencies(assert_array):
      p = self._dist_to_opt_avg**2 * self._h_min**2 / 2 / self._grad_var
      w3 = (-tf.sqrt(p**2 + 4.0 / 27.0 * p**3) - p) / 2.0
      w = tf.sign(w3) * tf.pow(tf.abs(w3), 1.0/3.0)
      y = w - p / 3.0 / w
      x = y + 1
    return x