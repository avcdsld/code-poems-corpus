function lockFirstScreen () {
  // when is prerendering, iframe container display none,
  // all elements are not in viewport.
  if (prerender.isPrerendering) {
    return
  }
  let viewportRect = viewport.getRect()
  fsElements = fsElements.filter((element) => {
    if (prerender.isPrerendered) {
      return element._resources.isInViewport(element, viewportRect)
    }
    return element.inViewport()
  }).map((element) => {
    element.setAttribute('mip-firstscreen-element', '')
    return element
  })
  fsElementsLocked = true
  tryRecordFirstScreen()
  !prerender.isPrerendered && firstScreenLabel.sendLog()
}