@Override
	public void register(Metric metric, String metricName, AbstractMetricGroup group) {
		synchronized (lock) {
			if (isShutdown()) {
				LOG.warn("Cannot register metric, because the MetricRegistry has already been shut down.");
			} else {
				if (reporters != null) {
					for (int i = 0; i < reporters.size(); i++) {
						MetricReporter reporter = reporters.get(i);
						try {
							if (reporter != null) {
								FrontMetricGroup front = new FrontMetricGroup<AbstractMetricGroup<?>>(i, group);
								reporter.notifyOfAddedMetric(metric, metricName, front);
							}
						} catch (Exception e) {
							LOG.warn("Error while registering metric.", e);
						}
					}
				}
				try {
					if (queryService != null) {
						queryService.addMetric(metricName, metric, group);
					}
				} catch (Exception e) {
					LOG.warn("Error while registering metric.", e);
				}
				try {
					if (metric instanceof View) {
						if (viewUpdater == null) {
							viewUpdater = new ViewUpdater(executor);
						}
						viewUpdater.notifyOfAddedView((View) metric);
					}
				} catch (Exception e) {
					LOG.warn("Error while registering metric.", e);
				}
			}
		}
	}