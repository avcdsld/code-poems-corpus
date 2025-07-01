function _initModules() {
  const modules = store.modules;

  Object.keys(modules).forEach(function(key) {
    if (typeof modules[key].onRegisterCallback === 'function') {
      modules[key].onRegisterCallback();
    }
  });
}