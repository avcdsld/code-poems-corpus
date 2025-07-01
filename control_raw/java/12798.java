public String optString(String key, String defaultValue) {
    Object o = opt(key);
    return o != null ? o.toString() : defaultValue;
  }