function isFirstLegendChildOfFieldset(element, parent) {
  return (
    getTag(element) === 'legend' &&
    getTag(parent) === 'fieldset' &&
    element.isSameNode(
      Array.from(parent.children).find(child => getTag(child) === 'legend'),
    )
  )
}