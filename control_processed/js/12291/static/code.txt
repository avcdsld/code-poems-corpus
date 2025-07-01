function() {
    if (!argv.analytics) { return []; } // empty arrays won't affect a standard build

    const directoryContents = fs.readdirSync(ANALYTICS_PATH);
    return directoryContents
      .filter(file => isModuleDirectory(path.join(ANALYTICS_PATH, file)))
      .map(moduleDirectory => {
        const module = require(path.join(ANALYTICS_PATH, moduleDirectory, MANIFEST));
        return path.join(ANALYTICS_PATH, moduleDirectory, module.main);
      });
  }