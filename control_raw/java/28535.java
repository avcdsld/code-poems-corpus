public static ListValue of(FullEntity<?> first, FullEntity<?>... other) {
    return newBuilder().addValue(first, other).build();
  }