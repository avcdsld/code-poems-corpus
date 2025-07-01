@CheckReturnValue
    public static <T> T mock(Class<T> classToMock, String name) {
        return mock(classToMock, withSettings()
                .name(name)
                .defaultAnswer(RETURNS_DEFAULTS));
    }