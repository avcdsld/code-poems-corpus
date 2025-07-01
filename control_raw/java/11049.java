public static @CheckForNull <T extends Descriptor> T find(Collection<? extends T> list, String string) {
        T d = findByClassName(list, string);
        if (d != null) {
                return d;
        }
        return findById(list, string);
    }