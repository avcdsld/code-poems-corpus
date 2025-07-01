public void putCachedAttributesFor(final RegisteredService registeredService,
                                       final CachingPrincipalAttributesRepository repository,
                                       final String id, final Map<String, List<Object>> attributes) {
        val cache = getRegisteredServiceCacheInstance(registeredService, repository);
        cache.put(id, attributes);
    }