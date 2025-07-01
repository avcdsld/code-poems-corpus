def timit_generator(data_dir,
                    tmp_dir,
                    training,
                    how_many,
                    start_from=0,
                    eos_list=None,
                    vocab_filename=None,
                    vocab_size=0):
  """Data generator for TIMIT transcription problem.

  Args:
    data_dir: path to the data directory.
    tmp_dir: path to temporary storage directory.
    training: a Boolean; if true, we use the train set, otherwise the test set.
    how_many: how many inputs and labels to generate.
    start_from: from which input to start.
    eos_list: optional list of end of sentence tokens, otherwise use default
      value `1`.
    vocab_filename: file within `tmp_dir` to read vocabulary from. If this is
      not provided then the target sentence will be encoded by character.
    vocab_size: integer target to generate vocabulary size to.

  Yields:
    A dictionary representing the images with the following fields:
    * inputs: a float sequence containing the audio data
    * audio/channel_count: an integer
    * audio/sample_count: an integer
    * audio/sample_width: an integer
    * targets: an integer sequence representing the encoded sentence
  """
  del data_dir
  eos_list = [1] if eos_list is None else eos_list
  if vocab_filename is not None:
    # TODO(lukaszkaiser): Correct this call to generate a vocabulary. No data
    # sources are being passed.
    # vocab_symbolizer = generator_utils.get_or_generate_vocab(
    #     data_dir, tmp_dir, vocab_filename, vocab_size)
    del vocab_size
    vocab_symbolizer = None
    assert False
  _get_timit(tmp_dir)
  datasets = (_TIMIT_TRAIN_DATASETS if training else _TIMIT_TEST_DATASETS)
  i = 0
  for timit_data_dir, (audio_ext, transcription_ext) in datasets:
    timit_data_dir = os.path.join(tmp_dir, timit_data_dir)
    data_files = _collect_data(timit_data_dir, audio_ext, transcription_ext)
    data_pairs = data_files.values()
    for input_file, target_file in sorted(data_pairs)[start_from:]:
      if i == how_many:
        return
      i += 1
      audio_data, sample_count, sample_width, num_channels = _get_audio_data(
          input_file)
      text_data = _get_text_data(target_file)
      if vocab_filename is None:
        label = [ord(c) for c in text_data] + eos_list
      else:
        label = vocab_symbolizer.encode(text_data) + eos_list
      yield {
          "inputs": audio_data,
          "audio/channel_count": [num_channels],
          "audio/sample_count": [sample_count],
          "audio/sample_width": [sample_width],
          "targets": label
      }