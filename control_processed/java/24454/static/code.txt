private void handleChangeCleaningInterval(final HttpServletRequest req,
      final Map<String, Object> ret) {
    try {
      final long newInterval = getLongParam(req, STATS_MAP_CLEANINGINTERVAL);
      if (MetricReportManager.isAvailable()) {
        final MetricReportManager metricManager = MetricReportManager.getInstance();
        final InMemoryMetricEmitter memoryEmitter =
            extractInMemoryMetricEmitter(metricManager);
        memoryEmitter.setReportingInterval(newInterval);
        ret.put(STATUS_PARAM, RESPONSE_SUCCESS);
      } else {
        ret.put(RESPONSE_ERROR, "MetricManager is not available");
      }
    } catch (final Exception e) {
      logger.error(e);
      ret.put(RESPONSE_ERROR, e.getMessage());
    }
  }