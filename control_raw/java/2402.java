public static void checkVersion(DB db, StoreVersion newversion, ObjectMapper mapper) throws
      IOException {
    byte[] bytes = db.get(StoreVersion.KEY);
    if (bytes == null) {
      storeVersion(db, newversion, mapper);
    } else {
      StoreVersion version = mapper.readValue(bytes, StoreVersion.class);
      if (version.major != newversion.major) {
        throw new IOException("cannot read state DB with version " + version + ", incompatible " +
            "with current version " + newversion);
      }
      storeVersion(db, newversion, mapper);
    }
  }