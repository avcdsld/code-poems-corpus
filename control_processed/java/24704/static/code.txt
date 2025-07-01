public void putLocal(final Props p) {
    for (final String key : p.localKeySet()) {
      this.put(key, p.get(key));
    }
  }