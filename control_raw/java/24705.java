public Class<?> getClass(final String key) {
    try {
      if (containsKey(key)) {
        return Class.forName(get(key));
      } else {
        throw new UndefinedPropertyException("Missing required property '"
            + key + "'");
      }
    } catch (final ClassNotFoundException e) {
      throw new IllegalArgumentException(e);
    }
  }