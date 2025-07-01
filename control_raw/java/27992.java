void updateSegmentIndexOffset(long segmentId, long indexOffset) {
        boolean remove = indexOffset < 0;
        SegmentKeyCache cache;
        int generation;
        synchronized (this.segmentCaches) {
            generation = this.currentCacheGeneration;
            if (remove) {
                cache = this.segmentCaches.remove(segmentId);
            } else {
                cache = this.segmentCaches.computeIfAbsent(segmentId, s -> new SegmentKeyCache(s, this.cache));
            }
        }

        if (cache != null) {
            if (remove) {
                evict(cache.evictAll());
            } else {
                cache.setLastIndexedOffset(indexOffset, generation);
            }
        }
    }