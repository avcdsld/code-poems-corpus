function indexOf(items, item) {
    var len = items.length, i;
    for (i = 0; i < len; i++) {
      if (items[i] === item) {
        return i;
      }
    }
    return -1;
  }