void initialCapacity(String key, @Nullable String value) {
    requireArgument(initialCapacity == UNSET_INT,
        "initial capacity was already set to %,d", initialCapacity);
    initialCapacity = parseInt(key, value);
  }