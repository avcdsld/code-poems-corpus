public static <K, T, V> MultiDimensionalMap<K, T, V> newHashBackedMap() {
        return new MultiDimensionalMap<>(new HashMap<Pair<K, T>, V>());
    }