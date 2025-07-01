def lengths_to_area_mask(feature_length, length, max_area_size):
  """Generates a non-padding mask for areas based on lengths.

  Args:
    feature_length: a tensor of [batch_size]
    length: the length of the batch
    max_area_size: the maximum area size considered
  Returns:
    mask: a tensor in shape of [batch_size, num_areas]
  """

  paddings = tf.cast(tf.expand_dims(
      tf.logical_not(
          tf.sequence_mask(feature_length, maxlen=length)), 2), tf.float32)
  _, _, area_sum, _, _ = compute_area_features(paddings,
                                               max_area_width=max_area_size)
  mask = tf.squeeze(tf.logical_not(tf.cast(area_sum, tf.bool)), [2])
  return mask