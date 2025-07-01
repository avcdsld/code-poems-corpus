public static ListValue of(String first, String... other) {
    return newBuilder().addValue(first, other).build();
  }