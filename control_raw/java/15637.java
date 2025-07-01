public void add(
      double value
  )
  {
    readWriteLock.writeLock().lock();

    try {
      if (value < lowerLimit) {
        outlierHandler.handleOutlierAdd(false);
        return;
      } else if (value >= upperLimit) {
        outlierHandler.handleOutlierAdd(true);
        return;
      }

      count += 1;
      if (value > max) {
        max = value;
      }
      if (value < min) {
        min = value;
      }

      double valueRelativeToRange = value - lowerLimit;
      int targetBucket = (int) (valueRelativeToRange / bucketSize);

      if (targetBucket >= histogram.length) {
        targetBucket = histogram.length - 1;
      }

      histogram[targetBucket] += 1;
    }
    finally {
      readWriteLock.writeLock().unlock();
    }
  }