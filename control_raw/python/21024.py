def op(name,
       data,
       display_name=None,
       description=None,
       collections=None):
  """Create a legacy text summary op.

  Text data summarized via this plugin will be visible in the Text Dashboard
  in TensorBoard. The standard TensorBoard Text Dashboard will render markdown
  in the strings, and will automatically organize 1D and 2D tensors into tables.
  If a tensor with more than 2 dimensions is provided, a 2D subarray will be
  displayed along with a warning message. (Note that this behavior is not
  intrinsic to the text summary API, but rather to the default TensorBoard text
  plugin.)

  Args:
    name: A name for the generated node. Will also serve as a series name in
      TensorBoard.
    data: A string-type Tensor to summarize. The text must be encoded in UTF-8.
    display_name: Optional name for this summary in TensorBoard, as a
      constant `str`. Defaults to `name`.
    description: Optional long-form description for this summary, as a
      constant `str`. Markdown is supported. Defaults to empty.
    collections: Optional list of ops.GraphKeys. The collections to which to add
      the summary. Defaults to [Graph Keys.SUMMARIES].

  Returns:
    A TensorSummary op that is configured so that TensorBoard will recognize
    that it contains textual data. The TensorSummary is a scalar `Tensor` of
    type `string` which contains `Summary` protobufs.

  Raises:
    ValueError: If tensor has the wrong type.
  """
  # TODO(nickfelt): remove on-demand imports once dep situation is fixed.
  import tensorflow.compat.v1 as tf

  if display_name is None:
    display_name = name
  summary_metadata = metadata.create_summary_metadata(
      display_name=display_name, description=description)
  with tf.name_scope(name):
    with tf.control_dependencies([tf.assert_type(data, tf.string)]):
      return tf.summary.tensor_summary(name='text_summary',
                                       tensor=data,
                                       collections=collections,
                                       summary_metadata=summary_metadata)