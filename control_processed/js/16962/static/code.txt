function getNodeSlots (element) {
  let nodeSlots = [...element.childNodes]
    .map(node => {
      element.removeChild(node)
      return node
    })

  return nodeSlots
}