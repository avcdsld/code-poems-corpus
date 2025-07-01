public static long zip(File directory, OutputStream out) throws IOException
  {
    if (!directory.isDirectory()) {
      throw new IOE("directory[%s] is not a directory", directory);
    }

    final ZipOutputStream zipOut = new ZipOutputStream(out);

    long totalSize = 0;
    for (File file : directory.listFiles()) {
      log.info("Adding file[%s] with size[%,d].  Total size so far[%,d]", file, file.length(), totalSize);
      if (file.length() > Integer.MAX_VALUE) {
        zipOut.finish();
        throw new IOE("file[%s] too large [%,d]", file, file.length());
      }
      zipOut.putNextEntry(new ZipEntry(file.getName()));
      totalSize += Files.asByteSource(file).copyTo(zipOut);
    }
    zipOut.closeEntry();
    // Workaround for http://hg.openjdk.java.net/jdk8/jdk8/jdk/rev/759aa847dcaf
    zipOut.flush();
    zipOut.finish();

    return totalSize;
  }