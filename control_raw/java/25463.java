public static Frame track(Frame... frames) {
    for (Frame fr : frames) {
      Scope scope = _scope.get();
      assert scope != null;
      track_impl(scope, fr._key);
      for (Vec vec : fr.vecs())
        track_impl(scope, vec._key);
    }
    return frames[0];
  }

  static private void track_impl(Scope scope, Key key) {
    if (key == null) return;
    // key size is 0 when tracked in the past, but no scope now
    if (scope._keys.size() > 0 && !scope._keys.peek().contains(key))
      scope._keys.peek().add(key);            // Track key
  }

  static public void untrack(Key<Vec>... keys) {
    Scope scope = _scope.get();           // Pay the price of T.L.S. lookup
    if (scope == null) return;           // Not tracking this thread
    if (scope._keys.size() == 0) return; // Tracked in the past, but no scope now
    HashSet<Key> xkeys = scope._keys.peek();
    for (Key<Vec> key : keys) xkeys.remove(key); // Untrack key
  }

  static public void untrack(Iterable<Key<Vec>> keys) {
    Scope scope = _scope.get();           // Pay the price of T.L.S. lookup
    if (scope == null) return;           // Not tracking this thread
    if (scope._keys.size() == 0) return; // Tracked in the past, but no scope now
    HashSet<Key> xkeys = scope._keys.peek();
    for (Key<Vec> key : keys) xkeys.remove(key); // Untrack key
  }
}