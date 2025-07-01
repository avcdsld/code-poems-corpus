public static ThreadFactory getThreadFactory(String nameFormat, boolean daemon) {
    if (IS_RESTRICTED_APPENGINE) {
      @SuppressWarnings("BetaApi")
      ThreadFactory factory = MoreExecutors.platformThreadFactory();
      return factory;
    } else {
      return new ThreadFactoryBuilder()
          .setDaemon(daemon)
          .setNameFormat(nameFormat)
          .build();
    }
  }