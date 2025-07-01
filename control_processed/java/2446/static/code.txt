void unregister(AbstractAppHandle handle) {
    for (Map.Entry<String, AbstractAppHandle> e : secretToPendingApps.entrySet()) {
      if (e.getValue().equals(handle)) {
        String secret = e.getKey();
        secretToPendingApps.remove(secret);
        break;
      }
    }

    unref();
  }