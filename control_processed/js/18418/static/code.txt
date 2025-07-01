function locateSeeds(sources, cwd) {
  sources = sources || [];
  cwd = cwd || process.cwd();

  const locations = sources.map((source) => path.join(cwd, source));
  return BbPromise.map(locations, (location) => {
    return fileExists(location).then((exists) => {
      if(!exists) {
        throw new Error("source file " + location + " does not exist");
      }
      return getSeedsAtLocation(location);
    });
  // Smash the arrays together
  }).then((seedArrays) => [].concat.apply([], seedArrays));
}