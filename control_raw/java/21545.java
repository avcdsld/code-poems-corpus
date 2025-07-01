@Incubating
    @CheckReturnValue
    public static <T> T spy(Class<T> classToSpy) {
        return MOCKITO_CORE.mock(classToSpy, withSettings()
                .useConstructor()
                .defaultAnswer(CALLS_REAL_METHODS));
    }