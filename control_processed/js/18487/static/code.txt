function log_level_plus(logLevel) {
  let index = log_levels.indexOf(logLevel)
  if (index < 0) {
    return []
  } else {
    return log_levels.slice(index, log_levels.length)
  }
}