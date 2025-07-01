@Nullable
  @WorkerThread
  Pair<FileExtension, InputStream> fetch() {
    File cachedFile = null;
    try {
      cachedFile = getCachedFile(url);
    } catch (FileNotFoundException e) {
      return null;
    }
    if (cachedFile == null) {
      return null;
    }

    FileInputStream inputStream;
    try {
      inputStream = new FileInputStream(cachedFile);
    } catch (FileNotFoundException e) {
      return null;
    }

    FileExtension extension;
    if (cachedFile.getAbsolutePath().endsWith(".zip")) {
      extension = FileExtension.ZIP;
    } else {
      extension = FileExtension.JSON;
    }

    L.debug("Cache hit for " + url + " at " + cachedFile.getAbsolutePath());
    return new Pair<>(extension, (InputStream) inputStream);
  }