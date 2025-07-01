function _initModulesOnElement(enabledElement) {
  const modules = store.modules;

  Object.keys(modules).forEach(function(key) {
    if (typeof modules[key].enabledElementCallback === 'function') {
      modules[key].enabledElementCallback(enabledElement);
    }
  });
}