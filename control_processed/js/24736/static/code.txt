function compare(a, b) {
  invariant(typeof a === typeof b, '"a" and "b" must be of the same type');

  if (a > b) {
    return 1;
  } else if (a < b) {
    return -1;
  } else {
    return 0;
  }
}