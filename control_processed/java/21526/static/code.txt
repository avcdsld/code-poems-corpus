public InternalRunner createStrict(Class<?> klass) throws InvocationTargetException {
        return create(klass, new Supplier<MockitoTestListener>() {
            public MockitoTestListener get() {
                return new MismatchReportingTestListener(Plugins.getMockitoLogger());
            }
        });
    }