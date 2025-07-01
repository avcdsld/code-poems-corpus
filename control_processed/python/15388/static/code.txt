def compute_classification_results(self, adv_batches, dataset_batches,
                                     dataset_meta, defense_work=None):
    """Computes classification results.

    Args:
      adv_batches: instance of AversarialBatches
      dataset_batches: instance of DatasetBatches
      dataset_meta: instance of DatasetMetadata
      defense_work: instance of DefenseWorkPieces

    Returns:
      accuracy_matrix, error_matrix, hit_target_class_matrix,
      processed_images_count
    """
    class_batch_to_work = {}
    if defense_work:
      for v in itervalues(defense_work.work):
        class_batch_to_work[v['output_classification_batch_id']] = v

    # accuracy_matrix[defense_id, attack_id] = num correctly classified
    accuracy_matrix = ResultMatrix()
    # error_matrix[defense_id, attack_id] = num misclassfied
    error_matrix = ResultMatrix()
    # hit_target_class_matrix[defense_id, attack_id] = num hit target class
    hit_target_class_matrix = ResultMatrix()
    # processed_images_count[defense_id] = num processed images by defense
    processed_images_count = {}

    total_count = len(self.data)
    processed_count = 0
    logging.info('Processing %d files with classification results',
                 len(self.data))
    for k, v in iteritems(self.data):
      if processed_count % 100 == 0:
        logging.info('Processed %d out of %d classification results',
                     processed_count, total_count)
      processed_count += 1
      defense_id = v['submission_id']
      adv_batch = adv_batches.data[v['adversarial_batch_id']]
      attack_id = adv_batch['submission_id']

      work_item = class_batch_to_work.get(k)
      required_work_stats = ['stat_correct', 'stat_error', 'stat_target_class',
                             'stat_num_images']
      if work_item and work_item['error']:
        # ignore batches with error
        continue
      if work_item and all(work_item.get(i) is not None
                           for i in required_work_stats):
        count_correctly_classified = work_item['stat_correct']
        count_errors = work_item['stat_error']
        count_hit_target_class = work_item['stat_target_class']
        num_images = work_item['stat_num_images']
      else:
        logging.warning('Recomputing accuracy for classification batch %s', k)
        (count_correctly_classified, count_errors, count_hit_target_class,
         num_images) = analyze_one_classification_result(
             self._storage_client, v['result_path'], adv_batch, dataset_batches,
             dataset_meta)

      # update accuracy and hit target class
      accuracy_matrix[defense_id, attack_id] += count_correctly_classified
      error_matrix[defense_id, attack_id] += count_errors
      hit_target_class_matrix[defense_id, attack_id] += count_hit_target_class
      # update number of processed images
      processed_images_count[defense_id] = (
          processed_images_count.get(defense_id, 0) + num_images)
    return (accuracy_matrix, error_matrix, hit_target_class_matrix,
            processed_images_count)