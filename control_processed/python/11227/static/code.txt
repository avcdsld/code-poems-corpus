def _checksum_paths():
  """Returns dict {'dataset_name': 'path/to/checksums/file'}."""
  dataset2path = {}
  for dir_path in _CHECKSUM_DIRS:
    for fname in _list_dir(dir_path):
      if not fname.endswith(_CHECKSUM_SUFFIX):
        continue
      fpath = os.path.join(dir_path, fname)
      dataset_name = fname[:-len(_CHECKSUM_SUFFIX)]
      dataset2path[dataset_name] = fpath
  return dataset2path