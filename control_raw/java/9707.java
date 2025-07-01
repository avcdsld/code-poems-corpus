public void configureLogging(LoggingPreferences prefs) {
    if (prefs == null) {
      return;
    }
    if (prefs.getEnabledLogTypes().contains(LogType.SERVER)) {
      serverLogLevel = prefs.getLevel(LogType.SERVER);
    }
  }