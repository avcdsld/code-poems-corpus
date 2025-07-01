function removeInvalidOptions(options, param) {
  const packageOptions = JSON.parse(JSON.stringify(options));
  if (options.platform === 'win32' && !isWindows()) {
    if (!hasBinary.sync('wine')) {
      log.warn(
        `Wine is required to use "${param}" option for a Windows app when packaging on non-windows platforms`,
      );
      packageOptions[param] = null;
    }
  }
  return packageOptions;
}