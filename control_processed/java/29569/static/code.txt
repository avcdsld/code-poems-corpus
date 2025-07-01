public static Value dateArray(@Nullable Iterable<Date> v) {
    return new DateArrayImpl(v == null, v == null ? null : immutableCopyOf(v));
  }