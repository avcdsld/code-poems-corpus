function toRules (cssText) {
  const node = parseCss(cssText)
  let rules = []

  if (node.rules && node.rules.length > 0) {
    rules = node.rules
      .filter(filterUnusedVendorRule)
      .map((rule) => toCssText(rule))
  } else {
    const cssText = toCssText(node)
    if (cssText) {
      rules = [cssText]
    }
  }

  return rules
}