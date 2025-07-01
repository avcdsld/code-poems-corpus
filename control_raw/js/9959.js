function getSVGElement(id) {
  var el = document.getElementById(id);
  return el ? assertInstanceof(el, Element) : null;
}