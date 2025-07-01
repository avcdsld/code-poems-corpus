public static RateLimiterMetricsCollector ofSupplier(MetricNames names, Supplier<? extends Iterable<? extends RateLimiter>> supplier) {
        return new RateLimiterMetricsCollector(names, supplier);
    }