def _prepare_sample_data(self, submission_type):
    """Prepares sample data for the submission.

    Args:
      submission_type: type of the submission.
    """
    # write images
    images = np.random.randint(0, 256,
                               size=[BATCH_SIZE, 299, 299, 3], dtype=np.uint8)
    for i in range(BATCH_SIZE):
      Image.fromarray(images[i, :, :, :]).save(
          os.path.join(self._sample_input_dir, IMAGE_NAME_PATTERN.format(i)))
    # write target class for targeted attacks
    if submission_type == 'targeted_attack':
      target_classes = np.random.randint(1, 1001, size=[BATCH_SIZE])
      target_class_filename = os.path.join(self._sample_input_dir,
                                           'target_class.csv')
      with open(target_class_filename, 'w') as f:
        for i in range(BATCH_SIZE):
          f.write((IMAGE_NAME_PATTERN + ',{1}\n').format(i, target_classes[i]))