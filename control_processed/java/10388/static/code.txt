private ValueCacheKey getRequestCacheKey(String cacheKey) {
        if (cacheKey != null) {
            /* create the cache key we will use to retrieve/store that include the type key prefix */
            return new ValueCacheKey(rcKey, cacheKey);
        }
        return null;
    }