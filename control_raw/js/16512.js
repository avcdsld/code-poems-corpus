function wrapModule(module, functions) {
  if (typeof module === 'string')
    module = require(module);

  if (!functions) {
    for (var k in module) {
      // HACK: wrap all functions with a fnSync variant.
      if (typeof module[k] === 'function' &&
          typeof module[k + 'Sync'] === 'function')
        module[k] = wrapFunction(module[k]);
    }
  } else {
    for (var i = 0, k; i < functions.length; i++) {
      var k = functions[i];
      module[k] = wrapFunction(module[k]);
    }
  }

  return module;
}