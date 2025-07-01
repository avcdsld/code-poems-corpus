def scaled_dot_product_attention_simple(q, k, v, bias, name=None):
  """Scaled dot-product attention. One head. One spatial dimension.

  Args:
    q: a Tensor with shape [batch, length_q, depth_k]
    k: a Tensor with shape [batch, length_kv, depth_k]
    v: a Tensor with shape [batch, length_kv, depth_v]
    bias: optional Tensor broadcastable to [batch, length_q, length_kv]
    name: an optional string

  Returns:
    A Tensor.
  """
  with tf.variable_scope(
      name, default_name="scaled_dot_product_attention_simple"):
    scalar = tf.rsqrt(tf.to_float(common_layers.shape_list(q)[2]))
    logits = tf.matmul(q * scalar, k, transpose_b=True)
    if bias is not None:
      logits += bias
    weights = tf.nn.softmax(logits, name="attention_weights")
    if common_layers.should_generate_summaries():
      tf.summary.image(
          "attention", tf.expand_dims(tf.pow(weights, 0.2), 3), max_outputs=1)
    return tf.matmul(weights, v)