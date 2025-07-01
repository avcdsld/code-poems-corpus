public static void putMethodCache(String serviceName, Method method) {
        ConcurrentHashMap<String, Method> cache = NOT_OVERLOAD_METHOD_CACHE.get(serviceName);
        if (cache == null) {
            cache = new ConcurrentHashMap<String, Method>();
            ConcurrentHashMap<String, Method> old = NOT_OVERLOAD_METHOD_CACHE.putIfAbsent(serviceName, cache);
            if (old != null) {
                cache = old;
            }
        }
        cache.putIfAbsent(method.getName(), method);
    }