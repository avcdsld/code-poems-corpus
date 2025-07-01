public static Set<String> killAllSpawnedHadoopJobs(String logFilePath, Logger log) {
    Set<String> allSpawnedJobs = findApplicationIdFromLog(logFilePath, log);
    log.info("applicationIds to kill: " + allSpawnedJobs);

    for (String appId : allSpawnedJobs) {
      try {
        killJobOnCluster(appId, log);
      } catch (Throwable t) {
        log.warn("something happened while trying to kill this job: " + appId, t);
      }
    }

    return allSpawnedJobs;
  }