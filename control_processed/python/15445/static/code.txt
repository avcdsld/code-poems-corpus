def filter(self, run_counts, criteria):
    """
    Return the counts for only those examples that are below the threshold
    """
    wrong_confidence = criteria['wrong_confidence']
    below_t = wrong_confidence <= self.t
    filtered_counts = deep_copy(run_counts)
    for key in filtered_counts:
      filtered_counts[key] = filtered_counts[key][below_t]
    return filtered_counts