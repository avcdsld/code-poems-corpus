def init_vq_bottleneck(bottleneck_size, hidden_size):
  """Get lookup table for VQ bottleneck."""
  means = tf.get_variable(
      name="means",
      shape=[bottleneck_size, hidden_size],
      initializer=tf.uniform_unit_scaling_initializer())
  ema_count = tf.get_variable(
      name="ema_count",
      shape=[bottleneck_size],
      initializer=tf.constant_initializer(0),
      trainable=False)
  with tf.colocate_with(means):
    ema_means = tf.get_variable(
        name="ema_means",
        initializer=means.initialized_value(),
        trainable=False)

  return means, ema_means, ema_count