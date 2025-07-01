def gather(params, indices, dtype=tf.float32):
  """Version of tf.gather that works faster on tpu."""
  if not is_xla_compiled():
    return tf.gather(params, indices)
  vocab_size = params.get_shape().as_list()[0]
  indices_flat = tf.reshape(indices, [-1])
  out = tf.matmul(tf.one_hot(indices_flat, vocab_size, dtype=dtype), params)
  out = reshape_like(out, tf.expand_dims(indices, -1))
  return out