public static InstrumentedExecutorService newFixedThreadPool(int nThreads, MetricRegistry registry) {
        return new InstrumentedExecutorService(Executors.newFixedThreadPool(nThreads), registry);
    }