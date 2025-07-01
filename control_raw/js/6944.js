function _createMaskConsumer() {
  const element = document.createElementNS(svgNS, 'rect');

  _setAttributes(element, {
    height: '100%',
    width: '100%',
    x: '0',
    y: '0'
  });
  element.setAttribute('mask', `url(#${elementIds.modalOverlayMask})`);

  return element;
}