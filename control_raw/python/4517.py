def tanh_discrete_bottleneck(x, bottleneck_bits, bottleneck_noise,
                             discretize_warmup_steps, mode):
  """Simple discretization through tanh, flip bottleneck_noise many bits."""
  x = tf.layers.dense(x, bottleneck_bits, name="tanh_discrete_bottleneck")
  d0 = tf.stop_gradient(2.0 * tf.to_float(tf.less(0.0, x))) - 1.0
  if mode == tf.estimator.ModeKeys.TRAIN:
    x += tf.truncated_normal(
        common_layers.shape_list(x), mean=0.0, stddev=0.2)
  x = tf.tanh(x)
  d = x + tf.stop_gradient(2.0 * tf.to_float(tf.less(0.0, x)) - 1.0 - x)
  if mode == tf.estimator.ModeKeys.TRAIN:
    noise = tf.random_uniform(common_layers.shape_list(x))
    noise = 2.0 * tf.to_float(tf.less(bottleneck_noise, noise)) - 1.0
    d *= noise
  d = common_layers.mix(d, x, discretize_warmup_steps,
                        mode == tf.estimator.ModeKeys.TRAIN)
  return d, d0