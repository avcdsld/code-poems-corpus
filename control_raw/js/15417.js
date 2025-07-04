function inspect(x) {
  if(x && isFunction(x.inspect)) {
    return ` ${x.inspect()}`
  }

  if(isFunction(x)) {
    return ' Function'
  }

  if(isArray(x)) {
    return ` [${arrayInspect(x) } ]`
  }

  if(isObject(x)) {
    return ` { ${Object.keys(x).reduce((acc, key) => {
      return acc.concat([ `${key}:${inspect(x[key])}` ])
    }, []).join(', ')} }`
  }

  if(isString(x)) {
    return ` "${x}"`
  }

  if(isSymbol(x) || isDate(x)) {
    return ` ${x.toString()}`
  }

  return ` ${x}`
}