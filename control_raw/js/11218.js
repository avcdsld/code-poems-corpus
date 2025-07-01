function buildRegExps(basePath, dirPaths) {
  return dirPaths.map(folderPath =>
    // Babel cares about windows/unix paths since v7b44
    // https://github.com/babel/babel/issues/8184
    // basePath + path.sep + dirPath/dirRegex
    // /home/name/webroot/js + / + relative/path/to/exclude
    // c:\home\name\webroot\js + \ + relative\path\to\exclude
    folderPath instanceof RegExp
      ? new RegExp(
          `^${escapeRegExp(path.resolve(basePath, '.') + path.sep)}${
            folderPath.source // This is actual regex, don't escape it
          }`,
          folderPath.flags,
        )
      : new RegExp('^' + escapeRegExp(path.resolve(basePath, folderPath))),
  );
}