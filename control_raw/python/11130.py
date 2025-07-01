def _generate_examples(self, file_paths):
    """Generate QuickDraw bitmap examples.

    Given a list of file paths with data for each class label, generate examples
    in a random order.

    Args:
      file_paths: (dict of {str: str}) the paths to files containing the data,
                  indexed by label.

    Yields:
      The QuickDraw examples, as defined in the dataset info features.
    """
    for label, path in sorted(file_paths.items(), key=lambda x: x[0]):
      with tf.io.gfile.GFile(path, "rb") as f:
        class_images = np.load(f)
        for np_image in class_images:
          yield {
              "image": np_image.reshape(_QUICKDRAW_IMAGE_SHAPE),
              "label": label,
          }