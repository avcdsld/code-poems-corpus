function objToString(obj, commentFix = false) {
  const comment = commentFix ? '/**/' : ''

  return Object.keys(obj).reduce((acc, k) => {
    let value = obj[k]

    if (k.startsWith('__spread__')) {
      return acc + '${' + value + '};' + comment
    }

    if (typeof value === 'string') {
      if (value[0] === '$') {
        value = '${' + value.substr(1) + '}'
      }
      return acc + camelToKebab(k) + ':' + value + ';' + comment
    } else {
      value = objToString(value)
      let key = k[0] === ':' ? '&' + k : k
      key = key[0] === '`' ? key.substr(1, key.length - 2) : key
      return acc + camelToKebab(key) + '{' + value + '};' + comment
    }
  }, '')
}