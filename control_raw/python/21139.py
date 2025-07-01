def _normalize_hparams(hparams):
  """Normalize a dict keyed by `HParam`s and/or raw strings.

  Args:
    hparams: A `dict` whose keys are `HParam` objects and/or strings
      representing hyperparameter names, and whose values are
      hyperparameter values. No two keys may have the same name.

  Returns:
    A `dict` whose keys are hyperparameter names (as strings) and whose
    values are the corresponding hyperparameter values.

  Raises:
    ValueError: If two entries in `hparams` share the same
      hyperparameter name.
  """
  result = {}
  for (k, v) in six.iteritems(hparams):
    if isinstance(k, HParam):
      k = k.name
    if k in result:
      raise ValueError("multiple values specified for hparam %r" % (k,))
    result[k] = v
  return result