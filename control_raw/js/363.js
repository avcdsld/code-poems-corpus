function sortFactory(key) {
  return function sortNumeric(a, b) {
    if (b[key] < a[key]) {
      return -1;
    }
    if (b[key] > a[key]) {
      return 1;
    }
    return 0;
  };
}