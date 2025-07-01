private boolean putIfAbsentNoAwait(K key, V value, boolean publishToWriter) {
    boolean[] absent = { false };
    cache.asMap().compute(copyOf(key), (k, expirable) -> {
      if ((expirable != null) && !expirable.isEternal()
          && expirable.hasExpired(currentTimeMillis())) {
        dispatcher.publishExpired(this, key, expirable.get());
        statistics.recordEvictions(1L);
        expirable = null;
      }
      if (expirable != null) {
        return expirable;
      }

      absent[0] = true;
      long expireTimeMS = getWriteExpireTimeMS(/* created */ true);
      if (expireTimeMS == 0) {
        return null;
      }
      if (publishToWriter) {
        publishToCacheWriter(writer::write, () -> new EntryProxy<>(key, value));
      }
      V copy = copyOf(value);
      dispatcher.publishCreated(this, key, copy);
      return new Expirable<>(copy, expireTimeMS);
    });
    return absent[0];
  }