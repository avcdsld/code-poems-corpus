function _setBooleanOption (key, val) {
  if (is.bool(val)) {
    this.options[key] = val;
  } else {
    throw new Error('Invalid ' + key + ' (boolean) ' + val);
  }
}