public Map<String, String> applyAll(Iterable<String> keys)
  {
    if (keys == null) {
      return Collections.emptyMap();
    }
    Map<String, String> map = new HashMap<>();
    for (String key : keys) {
      map.put(key, apply(key));
    }
    return map;
  }