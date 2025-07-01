@Override
  public PersistEntry[] list(String path) {
    final String bk[] = split(path);
    int substrLen = bk.length == 2 ? bk[1].length() : 0;
    List<PersistEntry> results = new ArrayList<>();
    try {
      for (Blob b : storageProvider.getStorage().list(bk[0]).iterateAll()) {
        if (bk.length == 1 || (bk.length == 2 && b.getName().startsWith(bk[1]))) {
          String relativeName = b.getName().substring(substrLen);
          if (relativeName.startsWith("/")) {
            relativeName = relativeName.substring(1);
          }
          results.add(new PersistEntry(relativeName, b.getSize(), b.getUpdateTime()));
        }
      }
    } catch (StorageException e) {
      Log.err(e);
    }
    return results.toArray(new PersistEntry[results.size()]);
  }