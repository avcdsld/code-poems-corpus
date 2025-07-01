function _cleanModulesOnElement(enabledElement) {
  const modules = store.modules;

  Object.keys(modules).forEach(function(key) {
    if (typeof modules[key].removeEnabledElementCallback === 'function') {
      modules[key].removeEnabledElementCallback(enabledElement);
    }
  });
}