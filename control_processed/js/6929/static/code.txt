function runLanguageHandler(src) {
  // execute source code in an isolated sandbox with a mock PR object
  var sandbox = createSandbox();
  vm.runInNewContext(fs.readFileSync(src), sandbox, {
    filename: src
  });

  // language name
  var lang = path.basename(src, path.extname(src)).replace(/^lang-/, '');

  // collect and filter extensions
  var exts = sandbox.extensions.map(function (ext) {
    // case-insensitive names
    return ext.toLowerCase();
  }).filter(function (ext) {
    // skip self, and internal names like foo-bar-baz or lang.foo
    return ext !== lang && !/\W/.test(ext);
  });
  exts = exts.filter(function (ext, pos) {
    // remove duplicates
    return exts.indexOf(ext) === pos;
  });
  return exts;
}