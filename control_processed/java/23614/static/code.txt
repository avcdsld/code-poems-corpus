public boolean isAllowed(String path) {
    for (String filter : STARTS_WITH_FILTER) {
      if (path.startsWith(filter)) {
        return false;
      }
    }
    for (String filter : CONTAINS_FILTER) {
      if (path.contains(filter)) {
        return false;
      }
    }
    return true;
  }