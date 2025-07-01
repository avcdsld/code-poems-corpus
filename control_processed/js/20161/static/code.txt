function containsActiveElement (el) {
  const node = el && findDOMNode(el)
  const active = getActiveElement()
  return (node && (active === node || contains(node,active)))
}