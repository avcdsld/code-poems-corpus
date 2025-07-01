def convert_videos_to_summaries(input_videos, output_videos, target_videos,
                                tag, decode_hparams,
                                display_ground_truth=False):
  """Converts input, output and target videos into video summaries.

  Args:
    input_videos: 5-D NumPy array, (NTHWC) conditioning frames.
    output_videos: 5-D NumPy array, (NTHWC) model predictions.
    target_videos: 5-D NumPy array, (NTHWC) target frames.
    tag: tf summary tag.
    decode_hparams: HParams.
    display_ground_truth: Whether or not to display ground truth videos.
  Returns:
    summaries: a list of tf frame-by-frame and video summaries.
  """
  fps = decode_hparams.frames_per_second
  border_percent = decode_hparams.border_percent
  max_outputs = decode_hparams.max_display_outputs
  target_steps = target_videos.shape[1]
  all_summaries = []
  input_videos = create_border(
      input_videos, color="blue", border_percent=border_percent)
  target_videos = create_border(
      target_videos, color="red", border_percent=border_percent)
  output_videos = create_border(
      output_videos, color="red", border_percent=border_percent)

  all_input = np.concatenate((input_videos, target_videos), axis=1)
  all_output = np.concatenate((input_videos, output_videos), axis=1)
  output_summ_vals, _ = common_video.py_gif_summary(
      "%s/output" % tag, all_output, max_outputs=max_outputs, fps=fps,
      return_summary_value=True)
  all_summaries.extend(output_summ_vals)

  # Optionally display ground truth.
  if display_ground_truth:
    input_summ_vals, _ = common_video.py_gif_summary(
        "%s/input" % tag, all_input, max_outputs=max_outputs, fps=fps,
        return_summary_value=True)
    all_summaries.extend(input_summ_vals)

  # Frame-by-frame summaries
  iterable = zip(output_videos[:max_outputs, :target_steps],
                 target_videos[:max_outputs])
  for ind, (input_video, output_video) in enumerate(iterable):
    t, h, w, c = input_video.shape
    # Tile vertically
    input_frames = np.reshape(input_video, (t*h, w, c))
    output_frames = np.reshape(output_video, (t*h, w, c))

    # Concat across width.
    all_frames = np.concatenate((input_frames, output_frames), axis=1)
    tag = "input/output/%s_sample_%d" % (tag, ind)
    frame_by_frame_summ = image_utils.image_to_tf_summary_value(
        all_frames, tag=tag)
    all_summaries.append(frame_by_frame_summ)
  return all_summaries