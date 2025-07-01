public static <T> T any(Class<T> type) {
        reportMatcher(new InstanceOf.VarArgAware(type, "<any " + type.getCanonicalName() + ">"));
        return defaultValue(type);
    }