public static ListValue of(LatLng first, LatLng... other) {
    return newBuilder().addValue(first, other).build();
  }