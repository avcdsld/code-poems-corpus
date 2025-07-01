public static InstrumentedExecutorService newFixedThreadPool(
            int nThreads, ThreadFactory threadFactory, MetricRegistry registry, String name) {
        return new InstrumentedExecutorService(Executors.newFixedThreadPool(nThreads, threadFactory), registry, name);
    }