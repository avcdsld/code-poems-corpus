function transformKeysToCamelCase (obj) {
  var camelKey;
  var key;
  for (key in obj) {
    camelKey = toCamelCase(key);
    if (key === camelKey) { continue; }
    obj[camelKey] = obj[key];
    delete obj[key];
  }
  return obj;
}