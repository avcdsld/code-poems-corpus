public static Value timestampArray(@Nullable Iterable<Timestamp> v) {
    return new TimestampArrayImpl(v == null, v == null ? null : immutableCopyOf(v));
  }