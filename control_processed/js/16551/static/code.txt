function compile(cmd, url) {
  var err = false;
  var reporter = {
    reportError: function(pos, msg) {
      err = true;

      var errMsg = util.format('%s:%s:%s %s', url, pos.line, pos.offset, msg);

      debug2('traceur-report-error: %s', errMsg);
      throw new Error(errMsg);
    },
    hadError: function() {
      return err;
    }
  };

  try {
    debug('traceur-input: %s', cmd);
    var InterceptOutputLoaderHooks = traceur.runtime.InterceptOutputLoaderHooks;
    var Loader = traceur.runtime.Loader;
    var loaderHooks = new InterceptOutputLoaderHooks(reporter, url);
    var loader = new Loader(loaderHooks);
    loader.script(cmd, {address: url});
    var output = loaderHooks.transcoded;
    debug('traceur-output: %s', output);
    return output;
  } catch(e) {
    debug3('traceur-compile-exception: %s', e.stack || e);

    if (parser && parser.isAtEnd())
      throw new SyntaxError('skip incomplete input');

    if (isWrapped(cmd))
      throw new SyntaxError('skip wrap');

    throw e;
  }
}