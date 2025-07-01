public static <T> T retryS3Operation(Task<T> f) throws Exception
  {
    final int maxTries = 10;
    return RetryUtils.retry(f, S3RETRY, maxTries);
  }