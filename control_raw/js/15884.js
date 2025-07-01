function head(foldable) {
    //  Fast path for arrays.
    if (Array.isArray (foldable)) {
      return foldable.length > 0 ? Just (foldable[0]) : Nothing;
    }
    return Z.reduce (function(m, x) { return m.isJust ? m : Just (x); },
                     Nothing,
                     foldable);
  }