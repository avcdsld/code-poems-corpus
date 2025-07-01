@VisibleForTesting
  static File getFile(String[] localDirs, int subDirsPerLocalDir, String filename) {
    int hash = JavaUtils.nonNegativeHash(filename);
    String localDir = localDirs[hash % localDirs.length];
    int subDirId = (hash / localDirs.length) % subDirsPerLocalDir;
    return new File(createNormalizedInternedPathname(
        localDir, String.format("%02x", subDirId), filename));
  }