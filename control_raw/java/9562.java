public OperaOptions addExtensions(List<File> paths) {
    for (File path : paths) {
      checkNotNull(path);
      checkArgument(path.exists(), "%s does not exist", path.getAbsolutePath());
      checkArgument(!path.isDirectory(), "%s is a directory",
          path.getAbsolutePath());
    }
    extensionFiles.addAll(paths);
    return this;
  }