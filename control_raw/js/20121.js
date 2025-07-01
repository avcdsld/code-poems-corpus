function _assign (maps) {
  let result = new Map()
  for (let m of maps) {
    for (let [key, value] of m) {
      if (result.has(key)) result.delete(key)
      result.set(key, value)
    }
  }
  return result
}