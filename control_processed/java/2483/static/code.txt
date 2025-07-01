public static <T> TypedColumn<T, Long> sumLong(MapFunction<T, Long> f) {
    return new TypedSumLong<T>(f).toColumnJava();
  }