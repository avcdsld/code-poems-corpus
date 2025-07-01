def _pack_with_custom_ops(dataset, keys, length):
  """Helper-function for packing a dataset which has already been batched.

  See pack_dataset()

  Relies on custom ops which require a custom compiled binary.
  Faster than _pack_with_tf_ops(), and denser packing.

  Args:
    dataset: a dataset containing padded batches of examples.
    keys: a list of strings (must have length 2)
    length: an integer

  Returns:
    a dataset.
  """
  from tensor2tensor.data_generators.ops import pack_sequences_ops  # pylint: disable=g-import-not-at-top
  # faster and better packing but requires custom-built binary.
  k1, k2 = keys
  def map_fn_custom(x):
    """Map-function."""
    (k1_packed, k1_segmengation, k1_position,
     k2_packed, k2_segmentation, k2_position) = (
         pack_sequences_ops.pack_sequences2(x[k1], x[k2], length))
    packed = {
        k1: k1_packed,
        k1 + "_segmentation": k1_segmengation,
        k1 + "_position": k1_position,
        k2: k2_packed,
        k2 + "_segmentation": k2_segmentation,
        k2 + "_position": k2_position,
    }
    return tf.data.Dataset.from_tensor_slices(packed)
  dataset = dataset.flat_map(map_fn_custom)
  return dataset