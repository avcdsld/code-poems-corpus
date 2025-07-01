@Override
  public synchronized void start() {
    if (isStarted()) {
      return;
    }
    MonitoredResource resource = getMonitoredResource(getProjectId());
    defaultWriteOptions =
        new WriteOption[] {WriteOption.logName(getLogName()), WriteOption.resource(resource)};
    getLogging().setFlushSeverity(severityFor(getFlushLevel()));
    loggingEnhancers = new ArrayList<>();
    List<LoggingEnhancer> resourceEnhancers = MonitoredResourceUtil.getResourceEnhancers();
    loggingEnhancers.addAll(resourceEnhancers);
    loggingEnhancers.addAll(getLoggingEnhancers());
    loggingEventEnhancers = new ArrayList<>();
    loggingEventEnhancers.addAll(getLoggingEventEnhancers());

    super.start();
  }