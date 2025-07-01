@CheckReturnValue
    public static <T> OngoingStubbing<T> when(T methodCall) {
        return MOCKITO_CORE.when(methodCall);
    }