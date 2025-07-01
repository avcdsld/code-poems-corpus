public static @Nonnull <T> List<T> unmodifiableList(@Nullable List<T> list) {
        if (isEmpty(list)) {
            return Collections.emptyList();
        }
        return Collections.unmodifiableList(list);
    }