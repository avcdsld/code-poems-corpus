public Application getRegisteredApplications(String appName) {
        return appNameApplicationMap.get(appName.toUpperCase(Locale.ROOT));
    }