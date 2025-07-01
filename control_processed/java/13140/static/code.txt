@Override public int compareTo(Annotation that) {
    if (this == that) return 0;
    int byTimestamp = timestamp() < that.timestamp() ? -1 : timestamp() == that.timestamp() ? 0 : 1;
    if (byTimestamp != 0) return byTimestamp;
    return value().compareTo(that.value());
  }