def text_embedding_column(key, module_spec, trainable=False):
  """Uses a Module to construct a dense representation from a text feature.

  This feature column can be used on an input feature whose values are strings
  of arbitrary size.

  The result of this feature column is the result of passing its `input`
  through the module `m` instantiated from `module_spec`, as per
  `result = m(input)`. The `result` must have dtype float32 and shape
  `[batch_size, num_features]` with a known value of num_features.

  Example:

  ```python
    comment = text_embedding_column("comment", "/tmp/text-module")
    feature_columns = [comment, ...]
    ...
    features = {
      "comment": np.array(["wow, much amazing", "so easy", ...]),
      ...
    }
    labels = np.array([[1], [0], ...])
    # If running TF 2.x, use `tf.compat.v1.estimator.inputs.numpy_input_fn`
    input_fn = tf.estimator.inputs.numpy_input_fn(features, labels,
                                                  shuffle=True)
    estimator = tf.estimator.DNNClassifier(hidden_units, feature_columns)
    estimator.train(input_fn, max_steps=100)
  ```

  Args:
    key: A string or `_FeatureColumn` identifying the text feature.
    module_spec: A ModuleSpec defining the Module to instantiate or a path where
      to load a ModuleSpec via `load_module_spec`
    trainable: Whether or not the Module is trainable. False by default,
      meaning the pre-trained weights are frozen. This is different from the
      ordinary tf.feature_column.embedding_column(), but that one is intended
      for training from scratch.

  Returns:
    `_DenseColumn` that converts from text input.

  Raises:
     ValueError: if module_spec is not suitable for use in this feature column.
  """
  module_spec = module.as_module_spec(module_spec)
  _check_module_is_text_embedding(module_spec)
  return _TextEmbeddingColumn(key=key, module_spec=module_spec,
                              trainable=trainable)