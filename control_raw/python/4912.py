def summarize_video(video, prefix, max_outputs=1):
  """Summarize the video using image summaries starting with prefix."""
  video_shape = shape_list(video)
  if len(video_shape) != 5:
    raise ValueError("Assuming videos given as tensors in the format "
                     "[batch, time, height, width, channels] but got one "
                     "of shape: %s" % str(video_shape))
  if tf.executing_eagerly():
    return
  if video.get_shape().as_list()[1] is None:
    tf.summary.image(
        "%s_last_frame" % prefix,
        tf.cast(video[:, -1, :, :, :], tf.uint8),
        max_outputs=max_outputs)
  else:
    for k in range(video_shape[1]):
      tf.summary.image(
          "%s_frame_%d" % (prefix, k),
          tf.cast(video[:, k, :, :, :], tf.uint8),
          max_outputs=max_outputs)