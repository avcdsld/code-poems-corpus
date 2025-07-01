function maybe_(thunk) {
    return function(f) {
      return function(maybe) {
        return maybe.isJust ? f (maybe.value) : thunk ();
      };
    };
  }