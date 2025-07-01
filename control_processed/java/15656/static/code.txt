private static FixedBucketsHistogram fromBytesSparse(ByteBuffer buf)
  {
    double lowerLimit = buf.getDouble();
    double upperLimit = buf.getDouble();
    int numBuckets = buf.getInt();
    OutlierHandlingMode outlierHandlingMode = OutlierHandlingMode.values()[buf.get()];

    long count = buf.getLong();
    long lowerOutlierCount = buf.getLong();
    long upperOutlierCount = buf.getLong();
    long missingValueCount = buf.getLong();

    double max = buf.getDouble();
    double min = buf.getDouble();

    int nonEmptyBuckets = buf.getInt();
    long histogram[] = new long[numBuckets];
    for (int i = 0; i < nonEmptyBuckets; i++) {
      int bucket = buf.getInt();
      long bucketCount = buf.getLong();
      histogram[bucket] = bucketCount;
    }

    return new FixedBucketsHistogram(
        lowerLimit,
        upperLimit,
        numBuckets,
        outlierHandlingMode,
        histogram,
        count,
        max,
        min,
        lowerOutlierCount,
        upperOutlierCount,
        missingValueCount
    );
  }