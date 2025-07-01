public static File getLogsRoot() {
        String tagsLogsPath = SystemProperties.getString(LOGS_ROOT_PATH_PROPERTY);
        if (tagsLogsPath == null) {
            return new File(Jenkins.get().getRootDir(), "logs");
        } else {
            Level logLevel = Level.INFO;
            if (ALREADY_LOGGED) {
                logLevel = Level.FINE;
            }
            LOGGER.log(logLevel,
                       "Using non default root path for tasks logging: {0}. (Beware: no automated migration if you change or remove it again)",
                       LOGS_ROOT_PATH_PROPERTY);
            ALREADY_LOGGED = true;
            return new File(tagsLogsPath);
        }
    }