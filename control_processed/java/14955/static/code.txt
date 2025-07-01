public static <T> T load(
      Class<T> klass,
      Iterable<Class<?>> hardcoded,
      ClassLoader cl,
      PriorityAccessor<T> priorityAccessor) {
    List<T> candidates = loadAll(klass, hardcoded, cl, priorityAccessor);
    if (candidates.isEmpty()) {
      return null;
    }
    return candidates.get(0);
  }