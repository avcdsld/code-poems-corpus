function htmlParse(value, config) {
  var allow

  if (Array.isArray(config)) {
    allow = config
  } else if (config) {
    allow = config.allow
  }

  return core(
    value,
    unified()
      .use(html)
      .use(rehype2retext, makeText(config))
      .use(filter, {allow: allow})
  )
}