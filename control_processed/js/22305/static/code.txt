function genModuleDeps(scriptPath) {
  var provideMap = new ProvideMap_();
  var requireMap = new RequireMap_();
  scanFiles([scriptPath], provideMap, requireMap);
  var dumpValues = function(map) {
    var results = [];
    map.forEach(function(value, key) {
      results = results.concat(value);
    });
    return results;
  };

  var relativePath = pathMod.join('../..', scriptPath);
  if (osMod.platform().indexOf('win') != -1) {
    relativePath = relativePath.replace(/\\/g, '\\\\');
  }

  var provide = provideMap.getAllProvides();
  var require = requireMap.getAllRequires();
  return 'goog.addDependency("' + relativePath + '", ' +
      JSON.stringify(dumpValues(provide)) + ', ' +
      JSON.stringify(dumpValues(require)) + ', true);';
}