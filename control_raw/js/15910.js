function match(pattern) {
    return function(s) {
      return Z.map (toMatch,
                    Z.reject (equals (null), Just (s.match (pattern))));
    };
  }