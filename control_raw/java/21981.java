protected com.github.benmanes.caffeine.cache.Cache buildCache(CacheConfiguration cacheConfiguration) {
        Caffeine<Object, Object> builder = Caffeine.newBuilder();
        cacheConfiguration.getExpireAfterAccess().ifPresent(duration -> builder.expireAfterAccess(duration.toMillis(), TimeUnit.MILLISECONDS));
        cacheConfiguration.getExpireAfterWrite().ifPresent(duration -> builder.expireAfterWrite(duration.toMillis(), TimeUnit.MILLISECONDS));
        cacheConfiguration.getInitialCapacity().ifPresent(builder::initialCapacity);
        cacheConfiguration.getMaximumSize().ifPresent(builder::maximumSize);
        cacheConfiguration.getMaximumWeight().ifPresent((long weight) -> {
            builder.maximumWeight(weight);
            builder.weigher(findWeigher());
        });
        if (cacheConfiguration.isRecordStats()) {
            builder.recordStats();
        }
        if (cacheConfiguration.isTestMode()) {
            // run commands on same thread
            builder.executor(Runnable::run);
        }
        return builder.build();
    }