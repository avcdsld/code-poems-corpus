def make_curve(report, success_name, fail_names):
  """
  Make a success-failure curve.
  :param report: A confidence report
    (the type of object saved by make_confidence_report.py)
  :param success_name: see plot_report_from_path
  :param fail_names: see plot_report_from_path
  :returns:
    fail_optimal: list of failure rates on adversarial data for the optimal
      (t >= .5) part of the curve. Each entry corresponds to a different
      threshold. Thresholds are chosen to make the smoothest possible curve
      from the available data, e.g. one threshold between each unique
      confidence value observed in the data. To make sure that linear
      interpolation between points in the curve never overestimates the
      failure rate for a specific success rate, the curve also includes
      extra points that increment the failure rate prior to any point
      that increments the success rate, so the curve moves up and to the
      right in a series of backwards "L" shapes rather than moving up
      and to the right along diagonal lines. For large datasets these
      maximally pessimistic points will usually not be visible and the
      curve will appear smooth.
    success_optimal: list of success rates on clean data on the optimal
      part of the curve. Matches up with `fail_optimal`.
    fail_lower_bound: list of observed failure rates on the t < .5 portion
      of the curve where MaxConfidence is not optimal.
    fail_upper_bound: list of upper bounds (assuming good enough optimization,
      so not a true upper bound) on the failure rates on the t < .5 portion
      of the curve where MaxConfidence is not optimal. Matches up with
      `fail_lower_bound`.
    success_bounded: success rates on the non-optimal part of the curve.
      Matches up with `fail_lower_bound` and `fail_upper_bound`.
  """
  success_results = report[success_name]
  fail_name = None # pacify pylint
  found = False
  for fail_name in fail_names:
    if fail_name in report:
      found = True
      break
  if not found:
    raise ValueError(fail_name + " not in report."
                     "Available keys: " + str(report.keys()))
  fail_results = report[fail_name]

  # "good" means drawn from the distribution where we measure success rate.
  # "bad" means drawn from the distribution where we measure failure rate.
  # From here on out we use those terms, to avoid confusion between examples
  # that actually failed and examples that were drawn from the distribution
  # where we measured failure rate.

  old_all_probs_version = False
  if isinstance(success_results, dict):
    # This dictionary key lookup will trigger a deprecation warning if `success_results` is not the old dictionary
    # style of report, so we don't want to do a dictionary lookup unless we really are using the old version.
    old_all_probs_version = 'all_probs' in success_results

  if old_all_probs_version:
    warnings.warn("The 'all_probs' key is included only to support "
                  " old files from a private development codebase. "
                  "Support for this key can be dropped at any time "
                  " without warning.")
    good_probs = success_results['all_probs']
    bad_probs = fail_results['all_probs']
    bad_corrects = fail_results['correctness_mask']
    good_corrects = success_results['correctness_mask']
  else:
    if isinstance(success_results, dict):
      # Still using dict, but using newer key names
      warnings.warn("Support for dictionary confidence reports is deprecated. Switch to using the classes in "
                    "cleverhans.confidence_report. Support for old dictionary-style reports may be removed "
                    "on or after 2019-07-19.")
      good_probs = success_results['confidence']
      bad_probs = fail_results['confidence']
      good_corrects = success_results['correctness']
      bad_corrects = fail_results['correctness']
    else:
      # current version
      good_probs = success_results.confidence
      bad_probs = fail_results.confidence
      good_corrects = success_results.correctness
      bad_corrects = fail_results.correctness
  good_triplets = [(prob, correct, True) for prob, correct
                   in safe_zip(good_probs, good_corrects)]
  bad_triplets = [(prob, correct, False) for prob, correct
                  in safe_zip(bad_probs, bad_corrects)]
  total_good = len(good_triplets)
  total_bad = len(bad_triplets)
  if total_good != 10000:
    warnings.warn("Not using full test set? Found " + str(total_good) +
                  " examples for measuring success rate")
  if total_bad != 10000:
    warnings.warn("Not using full test set for adversarial examples?")
  all_triplets = good_triplets + bad_triplets
  all_triplets = sorted(all_triplets, key=lambda x: -x[0])

  # Start with the case for threshold t = 1.
  # Examples are covered only if prob > t (strict inequality)
  # So initially nothing is covered
  good_covered_and_correct = 0
  bad_covered_and_incorrect = 0

  # Number of examples that are bad, incorrect, and covered by
  # a t >= 0.5, or that were merely covered by a t < 0.5
  failure_opportunities = 0

  next_idx = 0

  fail_optimal = []
  success_optimal = []
  fail_upper_bound = []
  fail_lower_bound = []
  success_bounded = []

  bounded = False

  # NOTE: the loop always exits via an internal break statement.
  # Copied the termination condition to the while statement for ease
  # of reading.
  while next_idx < len(all_triplets):
    gs = float(good_covered_and_correct) / total_good
    bf = float(bad_covered_and_incorrect) / total_bad
    # Add results for current threshold to the list
    if not bounded:

      # Sometimes when there are big jumps the failure rate it makes
      # artifacts in the plot, where there's a long linear track.
      # This implies the real success-fail curve is linear when
      # actually it just isn't sampled by the data.
      # To avoid implying that the model reaches a higher success
      # rate than it actually does, we avoid these plotting artifacts
      # by introducing extra points that make the graph move horizontally
      # to the right first, then vertically.
      if len(fail_optimal) > 0:
        prev_bf = fail_optimal[-1]
        prev_gs = success_optimal[-1]

        if gs > prev_gs and bf > prev_bf:
          fail_optimal.append(bf)
          success_optimal.append(prev_gs)

      success_optimal.append(gs)
      fail_optimal.append(bf)
    else:
      success_bounded.append(gs)
      fail_lower_bound.append(bf)
      fail_upper_bound.append(float(failure_opportunities) / total_bad)

    if next_idx == len(all_triplets):
      break

    # next_prob_to_include is not quite the same thing as the threshold.
    # The threshold is infinitesimally smaller than this value.
    next_prob_to_include = all_triplets[next_idx][0]

    # Process all ties
    while next_prob_to_include == all_triplets[next_idx][0]:
      _prob, correct, is_good = all_triplets[next_idx]
      if is_good:
        good_covered_and_correct += correct
      else:
        if next_prob_to_include <= .5:
          failure_opportunities += 1
        else:
          failure_opportunities += 1 - correct
        bad_covered_and_incorrect += 1 - correct
      next_idx += 1
      if next_idx == len(all_triplets):
        break

    if next_prob_to_include <= .5:
      bounded = True

  out = (fail_optimal, success_optimal, fail_lower_bound, fail_upper_bound,
         success_bounded)
  return out