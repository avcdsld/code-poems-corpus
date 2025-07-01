function forEach(callback /* , thisArg */) {
    var entries = getInternalParamsState(this).entries;
    var boundFunction = bind(callback, arguments.length > 1 ? arguments[1] : undefined, 3);
    var i = 0;
    var entry;
    while (i < entries.length) {
      entry = entries[i++];
      boundFunction(entry.value, entry.key, this);
    }
  }