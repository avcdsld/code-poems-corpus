@SuppressWarnings("unchecked")
  @Nullable
  public <T> T get(Key<T> key) {
    return (T) data.get(key);
  }