public ObjectPool<MemcachedClientIF> getObjectPool() {
        val pool = new GenericObjectPool<MemcachedClientIF>(this);
        pool.setMaxIdle(memcachedProperties.getMaxIdle());
        pool.setMinIdle(memcachedProperties.getMinIdle());
        pool.setMaxTotal(memcachedProperties.getMaxTotal());
        return pool;
    }