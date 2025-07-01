function forEach(fun, context, desc) {
  let entry;
  /* eslint-disable no-param-reassign */
  if (context === true) {
    desc = true;
    context = undefined;
  } else if (typeof context !== 'object') {
    context = this;
  }
  /* eslint-enable */
  if (desc) {
    entry = this.tail;
    while (entry) {
      fun.call(context, entry.key, entry.value, this);
      entry = entry.older;
    }
  } else {
    entry = this.head;
    while (entry) {
      fun.call(context, entry.key, entry.value, this);
      entry = entry.newer;
    }
  }
}