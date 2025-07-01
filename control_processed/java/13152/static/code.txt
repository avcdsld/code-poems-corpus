@VisibleForTesting
  void clear() {
    insertServiceName.clear();
    if (insertRemoteServiceName != null) insertRemoteServiceName.clear();
    insertSpanName.clear();
    indexer.clear();
    if (insertAutocompleteValue != null) insertAutocompleteValue.clear();
  }