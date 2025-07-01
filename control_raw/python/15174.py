def plot_report(report, success_name, fail_names, label=None,
                is_max_confidence=True,
                linewidth=LINEWIDTH,
                plot_upper_bound=True):
  """
  Plot a success fail curve from a confidence report
  :param report: A confidence report
    (the type of object saved by make_confidence_report.py)
  :param success_name: see plot_report_from_path
  :param fail_names: see plot_report_from_path
  :param label: see plot_report_from_path
  :param is_max_confidence: see plot_report_from_path
  :param linewidth: see plot_report_from_path
  """
  (fail_optimal, success_optimal, fail_lower_bound, fail_upper_bound,
   success_bounded) = make_curve(report, success_name, fail_names)
  assert len(fail_lower_bound) == len(fail_upper_bound)
  fail_optimal = np.array(fail_optimal)
  fail_lower_bound = np.array(fail_lower_bound)
  fail_upper_bound = np.array(fail_upper_bound)

  if is_max_confidence:
    p, = pyplot.plot(fail_optimal, success_optimal, label=label,
                     linewidth=linewidth)
    color = p.get_color()
    pyplot.plot(fail_lower_bound, success_bounded, '--', color=color)
    if plot_upper_bound:
      pyplot.plot(fail_upper_bound, success_bounded, '--', color=color)
  else:
    # If the attack was not MaxConfidence, then this whole curve is just
    # a loose lower bound
    all_fail = np.concatenate((fail_optimal, fail_lower_bound), axis=0)
    pyplot.plot(all_fail, success_optimal + success_bounded,
                '--', label=label, linewidth=linewidth)

  pyplot.xlabel("Failure rate on adversarial examples")
  pyplot.ylabel("Success rate on clean examples")
  gap = fail_upper_bound - fail_lower_bound
  if gap.size > 0:
    assert gap.min() >= 0.
    print("Max gap: ", gap.max())