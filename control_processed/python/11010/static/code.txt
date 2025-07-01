def subsets(self):
    """Subsets that make up each split of the dataset for the language pair."""
    source, target = self.builder_config.language_pair
    filtered_subsets = {}
    for split, ss_names in self._subsets.items():
      filtered_subsets[split] = []
      for ss_name in ss_names:
        ds = DATASET_MAP[ss_name]
        if ds.target != target or source not in ds.sources:
          logging.info(
              "Skipping sub-dataset that does not include language pair: %s",
              ss_name)
        else:
          filtered_subsets[split].append(ss_name)
    logging.info("Using sub-datasets: %s", filtered_subsets)
    return filtered_subsets