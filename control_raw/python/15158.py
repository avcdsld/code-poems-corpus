def deterministic_dict(normal_dict):
  """
  Returns a version of `normal_dict` whose iteration order is always the same
  """
  out = OrderedDict()
  for key in sorted(normal_dict.keys()):
    out[key] = normal_dict[key]
  return out