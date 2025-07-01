function resetPrefixTimeout(element) {
  if (element[prefixTimeoutKey]) {
    clearTimeout(element[prefixTimeoutKey]);
    element[prefixTimeoutKey] = false;
  }
}