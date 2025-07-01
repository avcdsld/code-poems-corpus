static String findJarsDir(String sparkHome, String scalaVersion, boolean failIfNotFound) {
    // TODO: change to the correct directory once the assembly build is changed.
    File libdir = new File(sparkHome, "jars");
    if (!libdir.isDirectory()) {
      libdir = new File(sparkHome, String.format("assembly/target/scala-%s/jars", scalaVersion));
      if (!libdir.isDirectory()) {
        checkState(!failIfNotFound,
          "Library directory '%s' does not exist; make sure Spark is built.",
          libdir.getAbsolutePath());
        return null;
      }
    }
    return libdir.getAbsolutePath();
  }