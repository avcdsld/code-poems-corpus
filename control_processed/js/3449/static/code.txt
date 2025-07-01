function (data) {
    var cache = this.cache;
    var cachedGeometry;
    var hash;

    // Skip all caching logic.
    if (data.skipCache) { return createGeometry(data); }

    // Try to retrieve from cache first.
    hash = this.hash(data);
    cachedGeometry = cache[hash];
    incrementCacheCount(this.cacheCount, hash);

    if (cachedGeometry) { return cachedGeometry; }

    // Create geometry.
    cachedGeometry = createGeometry(data);

    // Cache and return geometry.
    cache[hash] = cachedGeometry;
    return cachedGeometry;
  }