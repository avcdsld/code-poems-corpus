function positionAbsolutely(element, x, y, extraTransforms) {
  extraTransforms = extraTransforms || '';
  if (cssSupported()) {
    // Use CSS 3D transforms when the browser supports them.
    // A translateZ(0) transform improves performance on Chrome by creating a
    // new layer for the element, which prevents unnecessary repaints.
    var transform = 'translateX(' + decimal(x) + 'px) translateY(' + decimal(y) + 'px) translateZ(0) ' + extraTransforms;
    setTransform(element, transform);
  } else {
    // Fall back to absolute positioning.
    setPixelPosition(element, x, y);
  }
}