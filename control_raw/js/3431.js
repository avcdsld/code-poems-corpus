function checkComponentDefined (el, name) {
  // Check if element contains the component.
  if (el.components[name] && el.components[name].attrValue) { return true; }

  return isComponentMixedIn(name, el.mixinEls);
}