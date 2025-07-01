function internalSearchObject (obj, searchTerm, seen, depth) {
  if (depth > SEARCH_MAX_DEPTH) {
    return false
  }
  let match = false
  const keys = Object.keys(obj)
  let key, value
  for (let i = 0; i < keys.length; i++) {
    key = keys[i]
    value = obj[key]
    match = internalSearchCheck(searchTerm, key, value, seen, depth + 1)
    if (match) {
      break
    }
  }
  return match
}