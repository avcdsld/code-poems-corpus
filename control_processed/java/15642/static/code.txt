private void simpleInterpolateMerge(FixedBucketsHistogram otherHistogram)
  {
    double rangeStart = Math.max(lowerLimit, otherHistogram.getLowerLimit());
    double rangeEnd = Math.min(upperLimit, otherHistogram.getUpperLimit());

    int myCurBucket = (int) ((rangeStart - lowerLimit) / bucketSize);
    double myNextCursorBoundary = (myCurBucket + 1) * bucketSize + lowerLimit;
    double myCursor = rangeStart;

    int theirCurBucket = (int) ((rangeStart - otherHistogram.getLowerLimit()) / otherHistogram.getBucketSize());
    double theirNextCursorBoundary = (theirCurBucket + 1) * otherHistogram.getBucketSize() + otherHistogram.getLowerLimit();
    double theirCursor = rangeStart;

    double intraBucketStride = otherHistogram.getBucketSize() / otherHistogram.getHistogram()[theirCurBucket];

    myNextCursorBoundary = Math.min(myNextCursorBoundary, rangeEnd);
    theirNextCursorBoundary = Math.min(theirNextCursorBoundary, rangeEnd);

    outlierHandler.simpleInterpolateMergeHandleOutliers(otherHistogram, rangeStart, rangeEnd);

    double theirCurrentLowerBucketBoundary = theirCurBucket * otherHistogram.getBucketSize() + otherHistogram.getLowerLimit();

    while (myCursor < rangeEnd) {
      double needToConsume = myNextCursorBoundary - myCursor;
      double canConsumeFromOtherBucket = theirNextCursorBoundary - theirCursor;
      double toConsume = Math.min(needToConsume, canConsumeFromOtherBucket);

      // consume one of our bucket's worth of data from the other histogram
      while (needToConsume > 0) {
        double fractional = toConsume / otherHistogram.getBucketSize();
        double fractionalCount = otherHistogram.getHistogram()[theirCurBucket] * fractional;

        if (Math.round(fractionalCount) > 0) {
          // in this chunk from the other histogram bucket, calculate min and max interpolated values that would be added
          double minStride = Math.ceil(
              (theirCursor - (theirCurBucket * otherHistogram.getBucketSize() + otherHistogram.getLowerLimit()))
              / intraBucketStride
          );

          minStride *= intraBucketStride;
          minStride += theirCurrentLowerBucketBoundary;
          if (minStride >= theirCursor) {
            min = Math.min(minStride, min);
            max = Math.max(minStride, max);
          }

          double maxStride = Math.floor(
              (theirCursor + toConsume - (theirCurBucket * otherHistogram.getBucketSize()
                                          + otherHistogram.getLowerLimit())) / intraBucketStride
          );
          maxStride *= intraBucketStride;
          maxStride += theirCurrentLowerBucketBoundary;
          if (maxStride < theirCursor + toConsume) {
            max = Math.max(maxStride, max);
            min = Math.min(maxStride, min);
          }
        }

        histogram[myCurBucket] += Math.round(fractionalCount);
        count += Math.round(fractionalCount);

        needToConsume -= toConsume;
        theirCursor += toConsume;
        myCursor += toConsume;


        if (theirCursor >= rangeEnd) {
          break;
        }

        // we've crossed buckets in the other histogram
        if (theirCursor >= theirNextCursorBoundary) {
          theirCurBucket += 1;
          intraBucketStride = otherHistogram.getBucketSize() / otherHistogram.getHistogram()[theirCurBucket];
          theirCurrentLowerBucketBoundary = theirCurBucket * otherHistogram.getBucketSize() + otherHistogram.getLowerLimit();
          theirNextCursorBoundary = (theirCurBucket + 1) * otherHistogram.getBucketSize() + otherHistogram.getLowerLimit();
          theirNextCursorBoundary = Math.min(theirNextCursorBoundary, rangeEnd);
        }

        canConsumeFromOtherBucket = theirNextCursorBoundary - theirCursor;
        toConsume = Math.min(needToConsume, canConsumeFromOtherBucket);
      }

      if (theirCursor >= rangeEnd) {
        break;
      }

      myCurBucket += 1;
      myNextCursorBoundary = (myCurBucket + 1) * bucketSize + lowerLimit;
      myNextCursorBoundary = Math.min(myNextCursorBoundary, rangeEnd);
    }
  }