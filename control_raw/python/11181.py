def load_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Restore names if defined
    names_filepath = _get_names_filepath(data_dir, feature_name)
    if tf.io.gfile.exists(names_filepath):
      self.names = _load_names_from_file(names_filepath)