public static FileUtils.FileCopyResult gunzip(final ByteSource in, File outFile)
  {
    return gunzip(in, outFile, FileUtils.IS_EXCEPTION);
  }