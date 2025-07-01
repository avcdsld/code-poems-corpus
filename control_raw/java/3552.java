private AggregatedMetricsResponseBody getAggregatedMetricValues(
			Collection<? extends MetricStore.ComponentMetricStore> stores,
			List<String> requestedMetrics,
			MetricAccumulatorFactory requestedAggregationsFactories) {

		Collection<AggregatedMetric> aggregatedMetrics = new ArrayList<>(requestedMetrics.size());
		for (String requestedMetric : requestedMetrics) {
			final Collection<Double> values = new ArrayList<>(stores.size());
			try {
				for (MetricStore.ComponentMetricStore store : stores) {
					String stringValue = store.metrics.get(requestedMetric);
					if (stringValue != null) {
						values.add(Double.valueOf(stringValue));
					}
				}
			} catch (NumberFormatException nfe) {
				log.warn("The metric {} is not numeric and can't be aggregated.", requestedMetric, nfe);
				// metric is not numeric so we can't perform aggregations => ignore it
				continue;
			}
			if (!values.isEmpty()) {

				Iterator<Double> valuesIterator = values.iterator();
				MetricAccumulator acc = requestedAggregationsFactories.get(requestedMetric, valuesIterator.next());
				valuesIterator.forEachRemaining(acc::add);

				aggregatedMetrics.add(acc.get());
			} else {
				return new AggregatedMetricsResponseBody(Collections.emptyList());
			}
		}
		return new AggregatedMetricsResponseBody(aggregatedMetrics);
	}