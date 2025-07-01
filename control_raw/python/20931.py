def op(name,
       audio,
       sample_rate,
       labels=None,
       max_outputs=3,
       encoding=None,
       display_name=None,
       description=None,
       collections=None):
  """Create a legacy audio summary op for use in a TensorFlow graph.

  Arguments:
    name: A unique name for the generated summary node.
    audio: A `Tensor` representing audio data with shape `[k, t, c]`,
      where `k` is the number of audio clips, `t` is the number of
      frames, and `c` is the number of channels. Elements should be
      floating-point values in `[-1.0, 1.0]`. Any of the dimensions may
      be statically unknown (i.e., `None`).
    sample_rate: An `int` or rank-0 `int32` `Tensor` that represents the
      sample rate, in Hz. Must be positive.
    labels: Optional `string` `Tensor`, a vector whose length is the
      first dimension of `audio`, where `labels[i]` contains arbitrary
      textual information about `audio[i]`. (For instance, this could be
      some text that a TTS system was supposed to produce.) Markdown is
      supported. Contents should be UTF-8.
    max_outputs: Optional `int` or rank-0 integer `Tensor`. At most this
      many audio clips will be emitted at each step. When more than
      `max_outputs` many clips are provided, the first `max_outputs`
      many clips will be used and the rest silently discarded.
    encoding: A constant `str` (not string tensor) indicating the
      desired encoding. You can choose any format you like, as long as
      it's "wav". Please see the "API compatibility note" below.
    display_name: Optional name for this summary in TensorBoard, as a
      constant `str`. Defaults to `name`.
    description: Optional long-form description for this summary, as a
      constant `str`. Markdown is supported. Defaults to empty.
    collections: Optional list of graph collections keys. The new
      summary op is added to these collections. Defaults to
      `[Graph Keys.SUMMARIES]`.

  Returns:
    A TensorFlow summary op.

  API compatibility note: The default value of the `encoding`
  argument is _not_ guaranteed to remain unchanged across TensorBoard
  versions. In the future, we will by default encode as FLAC instead of
  as WAV. If the specific format is important to you, please provide a
  file format explicitly.
  """
  # TODO(nickfelt): remove on-demand imports once dep situation is fixed.
  import tensorflow  # for contrib
  import tensorflow.compat.v1 as tf

  if display_name is None:
    display_name = name
  if encoding is None:
    encoding = 'wav'

  if encoding == 'wav':
    encoding = metadata.Encoding.Value('WAV')
    encoder = functools.partial(tensorflow.contrib.ffmpeg.encode_audio,
                                samples_per_second=sample_rate,
                                file_format='wav')
  else:
    raise ValueError('Unknown encoding: %r' % encoding)

  with tf.name_scope(name), \
       tf.control_dependencies([tf.assert_rank(audio, 3)]):
    limited_audio = audio[:max_outputs]
    encoded_audio = tf.map_fn(encoder, limited_audio,
                              dtype=tf.string,
                              name='encode_each_audio')
    if labels is None:
      limited_labels = tf.tile([''], tf.shape(input=limited_audio)[:1])
    else:
      limited_labels = labels[:max_outputs]
    tensor = tf.transpose(a=tf.stack([encoded_audio, limited_labels]))
    summary_metadata = metadata.create_summary_metadata(
        display_name=display_name,
        description=description,
        encoding=encoding)
    return tf.summary.tensor_summary(name='audio_summary',
                                     tensor=tensor,
                                     collections=collections,
                                     summary_metadata=summary_metadata)