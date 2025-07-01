static HystrixPlugins create(ClassLoader classLoader) {
        return new HystrixPlugins(classLoader, new LoggerSupplier() {
            @Override
            public Logger getLogger() {
                return LoggerFactory.getLogger(HystrixPlugins.class);
            }
        });
    }