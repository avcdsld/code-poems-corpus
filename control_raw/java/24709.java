public List<String> getStringList(final String key, final String sep) {
    final String val = get(key);
    if (val == null || val.trim().length() == 0) {
      return Collections.emptyList();
    }

    if (containsKey(key)) {
      return Arrays.asList(val.split(sep));
    } else {
      throw new UndefinedPropertyException("Missing required property '" + key
          + "'");
    }
  }