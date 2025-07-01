public static FileUtils.FileCopyResult gzip(final File inFile, final File outFile, Predicate<Throwable> shouldRetry)
  {
    gzip(Files.asByteSource(inFile), Files.asByteSink(outFile), shouldRetry);
    return new FileUtils.FileCopyResult(outFile);
  }