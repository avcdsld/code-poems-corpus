private static void _reset() {
        // clear metrics
        HystrixCommandMetrics.reset();
        HystrixThreadPoolMetrics.reset();
        HystrixCollapserMetrics.reset();
        // clear collapsers
        HystrixCollapser.reset();
        // clear circuit breakers
        HystrixCircuitBreaker.Factory.reset();
        HystrixPlugins.reset();
        HystrixPropertiesFactory.reset();
        currentCommand.set(new ConcurrentStack<HystrixCommandKey>());
    }