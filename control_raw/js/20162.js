function ms (val) {
  if (!val || typeof val === 'number') {
    return val
  }

  const [ num, unit ] = parseUnit(val)

  if (unit === 'ms') {
    return num
  } else if (unit === 's') {
    return num * 1000
  } else {
    return num
  }
}