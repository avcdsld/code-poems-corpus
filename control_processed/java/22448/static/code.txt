public static <T> T assertNotNull(T object, ExceptionType exceptionType, String message, Object... args) {
        if (object == null) {
            if (exceptionType == null) {
                exceptionType = ExceptionType.ILLEGAL_ARGUMENT;
            }

            throw exceptionType.newInstance(getMessage(message, args,
                                                       "[Assertion failed] - the argument is required; it must not be null"));
        }

        return object;
    }