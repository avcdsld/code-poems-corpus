def save(criteria, report, report_path, adv_x_val):
  """
  Saves the report and adversarial examples.
  :param criteria: dict, of the form returned by AttackGoal.get_criteria
  :param report: dict containing a confidence report
  :param report_path: string, filepath
  :param adv_x_val: numpy array containing dataset of adversarial examples
  """
  print_stats(criteria['correctness'], criteria['confidence'], 'bundled')

  print("Saving to " + report_path)
  serial.save(report_path, report)

  assert report_path.endswith(".joblib")
  adv_x_path = report_path[:-len(".joblib")] + "_adv.npy"
  np.save(adv_x_path, adv_x_val)