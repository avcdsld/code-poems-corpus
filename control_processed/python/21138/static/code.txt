def _make_pr_entry(self, step, wall_time, data_array, thresholds):
    """Creates an entry for PR curve data. Each entry corresponds to 1 step.

    Args:
      step: The step.
      wall_time: The wall time.
      data_array: A numpy array of PR curve data stored in the summary format.
      thresholds: An array of floating point thresholds.

    Returns:
      A PR curve entry.
    """
    # Trim entries for which TP + FP = 0 (precision is undefined) at the tail of
    # the data.
    true_positives = [int(v) for v in data_array[metadata.TRUE_POSITIVES_INDEX]]
    false_positives = [
        int(v) for v in data_array[metadata.FALSE_POSITIVES_INDEX]]
    tp_index = metadata.TRUE_POSITIVES_INDEX
    fp_index = metadata.FALSE_POSITIVES_INDEX
    positives = data_array[[tp_index, fp_index], :].astype(int).sum(axis=0)
    end_index_inclusive = len(positives) - 1
    while end_index_inclusive > 0 and positives[end_index_inclusive] == 0:
      end_index_inclusive -= 1
    end_index = end_index_inclusive + 1

    return {
        'wall_time': wall_time,
        'step': step,
        'precision': data_array[metadata.PRECISION_INDEX, :end_index].tolist(),
        'recall': data_array[metadata.RECALL_INDEX, :end_index].tolist(),
        'true_positives': true_positives[:end_index],
        'false_positives': false_positives[:end_index],
        'true_negatives':
            [int(v) for v in
             data_array[metadata.TRUE_NEGATIVES_INDEX][:end_index]],
        'false_negatives':
            [int(v) for v in
             data_array[metadata.FALSE_NEGATIVES_INDEX][:end_index]],
        'thresholds': thresholds[:end_index],
    }