private static String[] prepareDefaultConf() throws IOException {
    final File templateFolder = new File("test/local-conf-templates");
    final File localConfFolder = new File("local/conf");
    if (!localConfFolder.exists()) {
      FileUtils.copyDirectory(templateFolder, localConfFolder.getParentFile());
      log.info("Copied local conf templates from " + templateFolder.getAbsolutePath());
    }
    log.info("Using conf at " + localConfFolder.getAbsolutePath());
    return new String[]{"-conf", "local/conf"};
  }