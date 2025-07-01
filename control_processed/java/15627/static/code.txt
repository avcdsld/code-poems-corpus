@Nullable
  private static Long getValidTargetCompactionSizeBytes(
      @Nullable Long targetCompactionSizeBytes,
      @Nullable Integer maxRowsPerSegment,
      @Nullable UserCompactTuningConfig tuningConfig
  )
  {
    if (targetCompactionSizeBytes != null) {
      Preconditions.checkArgument(
          !hasPartitionConfig(maxRowsPerSegment, tuningConfig),
          "targetCompactionSizeBytes[%s] cannot be used with maxRowsPerSegment[%s] and maxTotalRows[%s]",
          targetCompactionSizeBytes,
          maxRowsPerSegment,
          tuningConfig == null ? null : tuningConfig.getMaxTotalRows()
      );
      return targetCompactionSizeBytes;
    } else {
      return hasPartitionConfig(maxRowsPerSegment, tuningConfig) ? null : DEFAULT_TARGET_COMPACTION_SIZE_BYTES;
    }
  }