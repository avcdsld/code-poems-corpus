def _file_num_records_cached(filename):
  """Return the number of TFRecords in a file."""
  # Cache the result, as this is expensive to compute
  if filename in _file_num_records_cache:
    return _file_num_records_cache[filename]
  ret = 0
  for _ in tf.python_io.tf_record_iterator(filename):
    ret += 1
  _file_num_records_cache[filename] = ret
  return ret