public final <R> Call<R> flatMap(FlatMapper<V, R> flatMapper) {
    return new FlatMapping<>(flatMapper, this);
  }