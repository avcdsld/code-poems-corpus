function setCell(map, key, columnCount, columnIndex, value) {
  if (!map.has(key)) map.set(key, new Array(columnCount));
  map.get(key)[columnIndex] = value;
}