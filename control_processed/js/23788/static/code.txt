function exec(paths, options) {
    ls.self = this;
    paths = paths !== null && !Array.isArray(paths) && (typeof paths === 'undefined' ? 'undefined' : _typeof(paths)) === 'object' ? paths.paths : paths;
    paths = paths || ['.'];
    paths = Array.isArray(paths) ? paths : [paths];
    paths = expand(paths);

    options = options || {};

    var preSortedPaths = ls.preSortPaths(paths);

    var dirResults = [];
    for (var i = 0; i < preSortedPaths.dirs.length; ++i) {
      if (options.recursive) {
        var result = ls.execDirRecursive(preSortedPaths.dirs[i], options);
        dirResults = dirResults.concat(result);
      } else {
        dirResults.push(ls.execDir(preSortedPaths.dirs[i], options));
      }
    }

    var stdout = '';
    if (preSortedPaths.files.length > 0) {
      stdout += ls.execLsOnFiles('.', preSortedPaths.files, options).results;
    }

    var dirOutput = ls.formatAll(dirResults, options, dirResults.length + preSortedPaths.files.length > 1);
    stdout += stdout && dirOutput ? '\n\n' + dirOutput : dirOutput;
    if (strip(stdout).trim() !== '') {
      ls.self.log(String(stdout).replace(/\\/g, '/'));
    }

    return 0;
  }