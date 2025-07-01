def export(export_path, vocabulary, embeddings, num_oov_buckets,
           preprocess_text):
  """Exports a TF-Hub module that performs embedding lookups.

  Args:
    export_path: Location to export the module.
    vocabulary: List of the N tokens in the vocabulary.
    embeddings: Numpy array of shape [N+K,M] the first N rows are the
      M dimensional embeddings for the respective tokens and the next K
      rows are for the K out-of-vocabulary buckets.
    num_oov_buckets: How many out-of-vocabulary buckets to add.
    preprocess_text: Whether to preprocess the input tensor by removing
      punctuation and splitting on spaces.
  """
  # Write temporary vocab file for module construction.
  tmpdir = tempfile.mkdtemp()
  vocabulary_file = os.path.join(tmpdir, "tokens.txt")
  with tf.gfile.GFile(vocabulary_file, "w") as f:
    f.write("\n".join(vocabulary))
  vocab_size = len(vocabulary)
  embeddings_dim = embeddings.shape[1]
  spec = make_module_spec(vocabulary_file, vocab_size, embeddings_dim,
                          num_oov_buckets, preprocess_text)

  try:
    with tf.Graph().as_default():
      m = hub.Module(spec)
      # The embeddings may be very large (e.g., larger than the 2GB serialized
      # Tensor limit).  To avoid having them frozen as constant Tensors in the
      # graph we instead assign them through the placeholders and feed_dict
      # mechanism.
      p_embeddings = tf.placeholder(tf.float32)
      load_embeddings = tf.assign(m.variable_map[EMBEDDINGS_VAR_NAME],
                                  p_embeddings)

      with tf.Session() as sess:
        sess.run([load_embeddings], feed_dict={p_embeddings: embeddings})
        m.export(export_path, sess)
  finally:
    shutil.rmtree(tmpdir)