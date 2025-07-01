public static PooledByteBufAllocator createPooledByteBufAllocator(
      boolean allowDirectBufs,
      boolean allowCache,
      int numCores) {
    if (numCores == 0) {
      numCores = Runtime.getRuntime().availableProcessors();
    }
    return new PooledByteBufAllocator(
      allowDirectBufs && PlatformDependent.directBufferPreferred(),
      Math.min(PooledByteBufAllocator.defaultNumHeapArena(), numCores),
      Math.min(PooledByteBufAllocator.defaultNumDirectArena(), allowDirectBufs ? numCores : 0),
      PooledByteBufAllocator.defaultPageSize(),
      PooledByteBufAllocator.defaultMaxOrder(),
      allowCache ? PooledByteBufAllocator.defaultTinyCacheSize() : 0,
      allowCache ? PooledByteBufAllocator.defaultSmallCacheSize() : 0,
      allowCache ? PooledByteBufAllocator.defaultNormalCacheSize() : 0,
      allowCache ? PooledByteBufAllocator.defaultUseCacheForAllThreads() : false
    );
  }