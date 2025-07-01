protected long computeOffset(final long t, final DateTimeZone tz)
  {
    // start is the beginning of the last period ending within dataInterval
    long start = dataInterval.getEndMillis() - periodMillis;
    long startOffset = start % periodMillis - originMillis % periodMillis;
    if (startOffset < 0) {
      startOffset += periodMillis;
    }

    start -= startOffset;

    // tOffset is the offset time t within the last period
    long tOffset = t % periodMillis - originMillis % periodMillis;
    if (tOffset < 0) {
      tOffset += periodMillis;
    }
    tOffset += start;
    return tOffset - t - (tz.getOffset(tOffset) - tz.getOffset(t));
  }