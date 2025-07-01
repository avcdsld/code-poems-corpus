public static void start(String[] args, String relativeResourcePath, boolean finalizeRestRegistration) {
    long time0 = System.currentTimeMillis();
    // Fire up the H2O Cluster
    H2O.main(args);

    H2O.registerResourceRoot(new File(relativeResourcePath + File.separator + "h2o-web/src/main/resources/www"));
    H2O.registerResourceRoot(new File(relativeResourcePath + File.separator + "h2o-core/src/main/resources/www"));
    ExtensionManager.getInstance().registerRestApiExtensions();
    if (!H2O.ARGS.disable_web) {
      if (finalizeRestRegistration) {
        H2O.startServingRestApi();
      }
    }

    long timeF = System.currentTimeMillis();
    Log.info("H2O started in " + (timeF - time0) + "ms");
    if (!H2O.ARGS.disable_web) {
      Log.info("");
      Log.info("Open H2O Flow in your web browser: " + H2O.getURL(NetworkInit.h2oHttpView.getScheme()));
      Log.info("");
    }
  }