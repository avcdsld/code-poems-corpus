private void doLoad() throws IOException {
    final String libName = getName();
    try {
      System.loadLibrary(libName);
    } catch (UnsatisfiedLinkError e) {
      try {
        extractAndLoad(getPlatformLibraryPath(), getSimpleLibraryPath());
      } catch (IOException ioe) {
        logger.warn("Failed to load library from both native path and jar!");
        throw ioe;
      }
    }
  }