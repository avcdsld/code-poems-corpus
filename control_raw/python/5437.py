def similarity_cost(inputs_encoded, targets_encoded):
  """Loss telling to be more similar to your own targets than to others."""
  # This is a first very simple version: handle variable-length by padding
  # to same length and putting everything into batch. In need of a better way.
  x, y = common_layers.pad_to_same_length(inputs_encoded, targets_encoded)
  depth = tf.shape(inputs_encoded)[3]
  x, y = tf.reshape(x, [-1, depth]), tf.reshape(y, [-1, depth])
  return rank_loss(x, y)