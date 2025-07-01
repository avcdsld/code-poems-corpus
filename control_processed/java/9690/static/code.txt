public void createLogFileAndAddToMap(SessionId sessionId) throws IOException {
    File rcLogFile;
    // create logFile;
    rcLogFile = File.createTempFile(sessionId.toString(), ".rclog");
    rcLogFile.deleteOnExit();
    LogFile logFile = new LogFile(rcLogFile.getAbsolutePath());
    sessionToLogFileMap.put(sessionId, logFile);
  }