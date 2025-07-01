function createInjector(options) {

  options = options || {};

  var configModule = {
    'config': ['value', options]
  };

  var modules = [ configModule, CoreModule ].concat(options.modules || []);

  return bootstrap(modules);
}