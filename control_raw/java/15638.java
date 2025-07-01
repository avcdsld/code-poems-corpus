public void combineHistogram(FixedBucketsHistogram otherHistogram)
  {
    if (otherHistogram == null) {
      return;
    }

    readWriteLock.writeLock().lock();
    otherHistogram.getReadWriteLock().readLock().lock();

    try {
      missingValueCount += otherHistogram.getMissingValueCount();

      if (bucketSize == otherHistogram.getBucketSize() &&
          lowerLimit == otherHistogram.getLowerLimit() &&
          upperLimit == otherHistogram.getUpperLimit()) {
        combineHistogramSameBuckets(otherHistogram);
      } else {
        combineHistogramDifferentBuckets(otherHistogram);
      }
    }
    finally {
      readWriteLock.writeLock().unlock();
      otherHistogram.getReadWriteLock().readLock().unlock();
    }
  }