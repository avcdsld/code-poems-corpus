function flattenArray(array, filter, map, result) {
  let index = -1;
  while (++index < array.length) {
    const value = array[index];
    if (Array.isArray(value)) {
      flattenArray(value, filter, map, result);
    } else if (filter(value)) {
      result.push(map(value));
    }
  }
  return result;
}