def attention_bias_same_segment(query_segment_id, memory_segment_id):
  """Create an bias tensor to be added to attention logits.

  Positions with the same segment_ids can see each other.

  Args:
    query_segment_id: a float `Tensor` with shape [batch, query_length].
    memory_segment_id: a float `Tensor` with shape [batch, memory_length].

  Returns:
    a `Tensor` with shape [batch, 1, query_length, memory_length].
  """
  ret = (tf.to_float(
      tf.not_equal(
          tf.expand_dims(query_segment_id, 2),
          tf.expand_dims(memory_segment_id, 1))) *
         large_compatible_negative(memory_segment_id.dtype))
  return tf.expand_dims(ret, axis=1)