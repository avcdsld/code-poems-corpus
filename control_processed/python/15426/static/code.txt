def compute_and_save_scores_and_ranking(attacks_output,
                                        defenses_output,
                                        dataset_meta,
                                        output_dir,
                                        save_all_classification=False):
  """Computes scores and ranking and saves it.

  Args:
    attacks_output: output of attacks, instance of AttacksOutput class.
    defenses_output: outputs of defenses. Dictionary of dictionaries, key in
      outer dictionary is name of the defense, key of inner dictionary is
      name of the image, value of inner dictionary is classification label.
    dataset_meta: dataset metadata, instance of DatasetMetadata class.
    output_dir: output directory where results will be saved.
    save_all_classification: If True then classification results of all
      defenses on all images produces by all attacks will be saved into
      all_classification.csv file. Useful for debugging.

  This function saves following files into output directory:
    accuracy_on_attacks.csv: matrix with number of correctly classified images
      for each pair of defense and attack.
    accuracy_on_targeted_attacks.csv: matrix with number of correctly classified
      images for each pair of defense and targeted attack.
    hit_target_class.csv: matrix with number of times defense classified image
      as specified target class for each pair of defense and targeted attack.
    defense_ranking.csv: ranking and scores of all defenses.
    attack_ranking.csv: ranking and scores of all attacks.
    targeted_attack_ranking.csv: ranking and scores of all targeted attacks.
    all_classification.csv: results of classification of all defenses on
      all images produced by all attacks. Only saved if save_all_classification
      argument is True.
  """
  def write_ranking(filename, header, names, scores):
    """Helper method which saves submissions' scores and names."""
    order = np.argsort(scores)[::-1]
    with open(filename, 'w') as f:
      writer = csv.writer(f)
      writer.writerow(header)
      for idx in order:
        writer.writerow([names[idx], scores[idx]])

  def write_score_matrix(filename, scores, row_names, column_names):
    """Helper method which saves score matrix."""
    result = np.pad(scores, ((1, 0), (1, 0)), 'constant').astype(np.object)
    result[0, 0] = ''
    result[1:, 0] = row_names
    result[0, 1:] = column_names
    np.savetxt(filename, result, fmt='%s', delimiter=',')

  attack_names = list(attacks_output.attack_names)
  attack_names_idx = {name: index for index, name in enumerate(attack_names)}
  targeted_attack_names = list(attacks_output.targeted_attack_names)
  targeted_attack_names_idx = {name: index
                               for index, name
                               in enumerate(targeted_attack_names)}
  defense_names = list(defenses_output.keys())
  defense_names_idx = {name: index for index, name in enumerate(defense_names)}

  # In the matrices below: rows - attacks, columns - defenses.
  accuracy_on_attacks = np.zeros(
      (len(attack_names), len(defense_names)), dtype=np.int32)
  accuracy_on_targeted_attacks = np.zeros(
      (len(targeted_attack_names), len(defense_names)), dtype=np.int32)
  hit_target_class = np.zeros(
      (len(targeted_attack_names), len(defense_names)), dtype=np.int32)

  for defense_name, defense_result in defenses_output.items():
    for image_filename, predicted_label in defense_result.items():
      attack_name, is_targeted, image_id = (
          attacks_output.image_by_base_filename(image_filename))
      true_label = dataset_meta.get_true_label(image_id)
      defense_idx = defense_names_idx[defense_name]
      if is_targeted:
        target_class = dataset_meta.get_target_class(image_id)
        if true_label == predicted_label:
          attack_idx = targeted_attack_names_idx[attack_name]
          accuracy_on_targeted_attacks[attack_idx, defense_idx] += 1
        if target_class == predicted_label:
          attack_idx = targeted_attack_names_idx[attack_name]
          hit_target_class[attack_idx, defense_idx] += 1
      else:
        if true_label == predicted_label:
          attack_idx = attack_names_idx[attack_name]
          accuracy_on_attacks[attack_idx, defense_idx] += 1

  # Save matrices.
  write_score_matrix(os.path.join(output_dir, 'accuracy_on_attacks.csv'),
                     accuracy_on_attacks, attack_names, defense_names)
  write_score_matrix(
      os.path.join(output_dir, 'accuracy_on_targeted_attacks.csv'),
      accuracy_on_targeted_attacks, targeted_attack_names, defense_names)
  write_score_matrix(os.path.join(output_dir, 'hit_target_class.csv'),
                     hit_target_class, targeted_attack_names, defense_names)

  # Compute and save scores and ranking of attacks and defenses,
  # higher scores are better.
  defense_scores = (np.sum(accuracy_on_attacks, axis=0)
                    + np.sum(accuracy_on_targeted_attacks, axis=0))
  attack_scores = (attacks_output.dataset_image_count * len(defenses_output)
                   - np.sum(accuracy_on_attacks, axis=1))
  targeted_attack_scores = np.sum(hit_target_class, axis=1)
  write_ranking(os.path.join(output_dir, 'defense_ranking.csv'),
                ['DefenseName', 'Score'], defense_names, defense_scores)
  write_ranking(os.path.join(output_dir, 'attack_ranking.csv'),
                ['AttackName', 'Score'], attack_names, attack_scores)
  write_ranking(
      os.path.join(output_dir, 'targeted_attack_ranking.csv'),
      ['AttackName', 'Score'], targeted_attack_names, targeted_attack_scores)

  if save_all_classification:
    with open(os.path.join(output_dir, 'all_classification.csv'), 'w') as f:
      writer = csv.writer(f)
      writer.writerow(['AttackName', 'IsTargeted', 'DefenseName', 'ImageId',
                       'PredictedLabel', 'TrueLabel', 'TargetClass'])
      for defense_name, defense_result in defenses_output.items():
        for image_filename, predicted_label in defense_result.items():
          attack_name, is_targeted, image_id = (
              attacks_output.image_by_base_filename(image_filename))
          true_label = dataset_meta.get_true_label(image_id)
          target_class = dataset_meta.get_target_class(image_id)
          writer.writerow([attack_name, is_targeted, defense_name, image_id,
                           predicted_label, true_label, target_class])