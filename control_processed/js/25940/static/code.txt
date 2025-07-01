function getInjectedValue(component, propertyName, source) {
  var value;
  var primitiveDefaults = source.defaultComponentsFromPrimitive || {};
  var aFrameDefaults = source.defaultComponents || {};
  var defaultSources = [primitiveDefaults, aFrameDefaults];
  for (var i = 0; value === undefined && i < defaultSources.length; i++) {
    var defaults = defaultSources[i];
    if (defaults.hasOwnProperty(component.name)) {
      if (!propertyName) {
        value = defaults[component.name];
      } else {
        value = defaults[component.name][propertyName];
      }
    }
  }
  return value;
}