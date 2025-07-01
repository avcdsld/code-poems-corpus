def actnorm_3d(name, x, logscale_factor=3.):
  """Applies actnorm to each time-step independently.

  There are a total of 2*n_channels*n_steps parameters learnt.

  Args:
    name: variable scope.
    x: 5-D Tensor, (NTHWC)
    logscale_factor: Increases the learning rate of the scale by
                     logscale_factor.
  Returns:
    x: 5-D Tensor, (NTHWC) with the per-timestep, per-channel normalization.
  """
  with tf.variable_scope(name, reuse=tf.AUTO_REUSE):
    x = tf.unstack(x, axis=1)
    x_normed = []
    for ind, x_step in enumerate(x):
      x_step, _ = actnorm("actnorm_%d" % ind, x_step,
                          logscale_factor=logscale_factor)
      x_normed.append(x_step)
    return tf.stack(x_normed, axis=1), None