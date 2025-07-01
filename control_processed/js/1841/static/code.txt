function match (el, selector) {
  if (!el || el.nodeType !== 1) return false
  if (vendor) return vendor.call(el, selector)
  var nodes = all(selector, el.parentNode)
  for (var i = 0; i < nodes.length; ++i) {
    if (nodes[i] === el) return true
  }
  return false
}