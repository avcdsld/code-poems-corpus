def _write_tfrecords_from_generator(generator, output_files, shuffle=True):
  """Writes generated str records to output_files in round-robin order."""
  if do_files_exist(output_files):
    raise ValueError(
        "Pre-processed files already exists: {}.".format(output_files))

  with _incomplete_files(output_files) as tmp_files:
    # Write all shards
    writers = [tf.io.TFRecordWriter(fname) for fname in tmp_files]
    with _close_on_exit(writers) as writers:
      logging.info("Writing TFRecords")
      _round_robin_write(writers, generator)
    # Shuffle each shard
    if shuffle:
      # WARNING: Using np instead of Python random because Python random
      # produce different values between Python 2 and 3 and between
      # architectures
      random_gen = np.random.RandomState(42)
      for path in utils.tqdm(
          tmp_files, desc="Shuffling...", unit=" shard", leave=False):
        _shuffle_tfrecord(path, random_gen=random_gen)