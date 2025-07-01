public Process launch() throws IOException {
    ProcessBuilder pb = createBuilder();

    boolean outputToLog = outputStream == null;
    boolean errorToLog = !redirectErrorStream && errorStream == null;

    String loggerName = getLoggerName();
    if (loggerName != null && outputToLog && errorToLog) {
      pb.redirectErrorStream(true);
    }

    Process childProc = pb.start();
    if (loggerName != null) {
      InputStream logStream = outputToLog ? childProc.getInputStream() : childProc.getErrorStream();
      new OutputRedirector(logStream, loggerName, REDIRECTOR_FACTORY);
    }

    return childProc;
  }