function getType (obj) {
  if (obj === null) {
    return '' + obj
  }
  if (isSymbol(obj)) {
    return 'symbol'
  }
  if (isDate(obj)) {
    return 'date'
  }
  if (isArray(obj)) {
    return 'array'
  }
  if (isRegExp(obj)) {
    return 'regexp'
  }
  if (isError(obj)) {
    return 'error'
  }
  return typeof obj
}