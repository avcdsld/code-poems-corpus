public static CircuitBreakerMetricsCollector ofSupplier(MetricNames names, Supplier<? extends Iterable<? extends CircuitBreaker>> supplier) {
        return new CircuitBreakerMetricsCollector(names, supplier);
    }