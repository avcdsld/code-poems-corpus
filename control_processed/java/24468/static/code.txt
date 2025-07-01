private void configureFlowLevelMetrics(final FlowRunner flowRunner) {
    logger.info("Configuring Azkaban metrics tracking for flow runner object");

    if (MetricReportManager.isAvailable()) {
      final MetricReportManager metricManager = MetricReportManager.getInstance();
      // Adding NumFailedFlow Metric listener
      flowRunner.addListener((NumFailedFlowMetric) metricManager
          .getMetricFromName(NumFailedFlowMetric.NUM_FAILED_FLOW_METRIC_NAME));
    }

  }