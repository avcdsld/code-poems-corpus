function isScalarAndEqual(valueA: mixed, valueB: mixed): boolean {
  return valueA === valueB && (valueA === null || typeof valueA !== 'object');
}