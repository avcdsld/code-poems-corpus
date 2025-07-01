@SuppressWarnings({ "unchecked" })
    /* package */<T> HystrixCachedObservable<T> putIfAbsent(String cacheKey, HystrixCachedObservable<T> f) {
        ValueCacheKey key = getRequestCacheKey(cacheKey);
        if (key != null) {
            /* look for the stored value */
            ConcurrentHashMap<ValueCacheKey, HystrixCachedObservable<?>> cacheInstance = requestVariableForCache.get(concurrencyStrategy);
            if (cacheInstance == null) {
                throw new IllegalStateException("Request caching is not available. Maybe you need to initialize the HystrixRequestContext?");
            }
            HystrixCachedObservable<T> alreadySet = (HystrixCachedObservable<T>) cacheInstance.putIfAbsent(key, f);
            if (alreadySet != null) {
                // someone beat us so we didn't cache this
                return alreadySet;
            }
        }
        // we either set it in the cache or do not have a cache key
        return null;
    }