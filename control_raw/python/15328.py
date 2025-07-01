def _verify_output(self, submission_type):
    """Verifies correctness of the submission output.

    Args:
      submission_type: type of the submission

    Returns:
      True if output looks valid
    """
    result = True
    if submission_type == 'defense':
      try:
        image_classification = load_defense_output(
            os.path.join(self._sample_output_dir, 'result.csv'))
        expected_keys = [IMAGE_NAME_PATTERN.format(i)
                         for i in range(BATCH_SIZE)]
        if set(image_classification.keys()) != set(expected_keys):
          logging.error('Classification results are not saved for all images')
          result = False
      except IOError as e:
        logging.error('Failed to read defense output file: %s', e)
        result = False
    else:
      for i in range(BATCH_SIZE):
        image_filename = os.path.join(self._sample_output_dir,
                                      IMAGE_NAME_PATTERN.format(i))
        try:
          img = np.array(Image.open(image_filename).convert('RGB'))
          if list(img.shape) != [299, 299, 3]:
            logging.error('Invalid image size %s for image %s',
                          str(img.shape), image_filename)
            result = False
        except IOError as e:
          result = False
    return result