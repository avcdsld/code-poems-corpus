public <V1, V2> Context withValues(Key<V1> k1, V1 v1, Key<V2> k2, V2 v2) {
    PersistentHashArrayMappedTrie<Key<?>, Object> newKeyValueEntries =
        keyValueEntries.put(k1, v1).put(k2, v2);
    return new Context(this, newKeyValueEntries);
  }