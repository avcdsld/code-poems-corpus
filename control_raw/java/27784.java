public void invalidateCache(String table, String key) {
        cache.invalidateCache(new TableCacheKey<>(table, key, x -> null));
    }