public static @CheckForNull <T> T lookup(Class<T> type) {
        Jenkins j = Jenkins.getInstanceOrNull();
        return j != null ? j.lookup.get(type) : null;
    }