def pb(name, data, bucket_count=None, display_name=None, description=None):
  """Create a legacy histogram summary protobuf.

  Arguments:
    name: A unique name for the generated summary, including any desired
      name scopes.
    data: A `np.array` or array-like form of any shape. Must have type
      castable to `float`.
    bucket_count: Optional positive `int`. The output will have this
      many buckets, except in two edge cases. If there is no data, then
      there are no buckets. If there is data but all points have the
      same value, then there is one bucket whose left and right
      endpoints are the same.
    display_name: Optional name for this summary in TensorBoard, as a
      `str`. Defaults to `name`.
    description: Optional long-form description for this summary, as a
      `str`. Markdown is supported. Defaults to empty.

  Returns:
    A `tf.Summary` protobuf object.
  """
  # TODO(nickfelt): remove on-demand imports once dep situation is fixed.
  import tensorflow.compat.v1 as tf

  if bucket_count is None:
    bucket_count = summary_v2.DEFAULT_BUCKET_COUNT
  data = np.array(data).flatten().astype(float)
  if data.size == 0:
    buckets = np.array([]).reshape((0, 3))
  else:
    min_ = np.min(data)
    max_ = np.max(data)
    range_ = max_ - min_
    if range_ == 0:
      center = min_
      buckets = np.array([[center - 0.5, center + 0.5, float(data.size)]])
    else:
      bucket_width = range_ / bucket_count
      offsets = data - min_
      bucket_indices = np.floor(offsets / bucket_width).astype(int)
      clamped_indices = np.minimum(bucket_indices, bucket_count - 1)
      one_hots = (np.array([clamped_indices]).transpose()
                  == np.arange(0, bucket_count))  # broadcast
      assert one_hots.shape == (data.size, bucket_count), (
          one_hots.shape, (data.size, bucket_count))
      bucket_counts = np.sum(one_hots, axis=0)
      edges = np.linspace(min_, max_, bucket_count + 1)
      left_edges = edges[:-1]
      right_edges = edges[1:]
      buckets = np.array([left_edges, right_edges, bucket_counts]).transpose()
  tensor = tf.make_tensor_proto(buckets, dtype=tf.float64)

  if display_name is None:
    display_name = name
  summary_metadata = metadata.create_summary_metadata(
      display_name=display_name, description=description)
  tf_summary_metadata = tf.SummaryMetadata.FromString(
      summary_metadata.SerializeToString())

  summary = tf.Summary()
  summary.value.add(tag='%s/histogram_summary' % name,
                    metadata=tf_summary_metadata,
                    tensor=tensor)
  return summary