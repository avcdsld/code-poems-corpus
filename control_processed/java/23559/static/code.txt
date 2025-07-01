@NonNull
  public static <K, V, K1 extends K, V1 extends V> LoadingCache<K1, V1> build(
      @NonNull Caffeine<K, V> builder,
      com.github.benmanes.caffeine.cache.@NonNull CacheLoader<? super K1, V1> loader) {
    return new CaffeinatedGuavaLoadingCache<>(builder.build(loader));
  }