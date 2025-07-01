public static Long getValidMaxTotalRows(IndexTuningConfig tuningConfig)
  {
    @Nullable final Integer numShards = tuningConfig.numShards;
    @Nullable final Long maxTotalRows = tuningConfig.maxTotalRows;
    if (numShards == null || numShards == -1) {
      return maxTotalRows == null ? IndexTuningConfig.DEFAULT_MAX_TOTAL_ROWS : maxTotalRows;
    } else {
      return null;
    }
  }