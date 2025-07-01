def zero_add(previous_value, x, name=None, reuse=None):
  """Resnet connection with zero initialization.

  Another type of resnet connection which returns previous_value + gamma * x.
  gamma is a trainable scalar and initialized with zero. It is useful when a
  module is plugged into a trained model and we want to make sure it matches the
  original model's performance.

  Args:
    previous_value:  A tensor.
    x: A tensor.
    name: name of variable scope; defaults to zero_add.
    reuse: reuse scope.

  Returns:
    previous_value + gamma * x.
  """
  with tf.variable_scope(name, default_name="zero_add", reuse=reuse):
    gamma = tf.get_variable("gamma", (), initializer=tf.zeros_initializer())
    return previous_value + gamma * x