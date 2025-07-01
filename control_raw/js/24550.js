function loadIconsFromDiskCache (loader, query, cacheFile, fileHash, callback) {
  // Stop if cache is disabled
  if (!query.persistentCache) return callback(null);
  var resolvedCacheFile = path.resolve(loader._compiler.parentCompilation.compiler.outputPath, cacheFile);

  fs.exists(resolvedCacheFile, function (exists) {
    if (!exists) return callback(null);
    fs.readFile(resolvedCacheFile, function (err, content) {
      if (err) return callback(err);
      var cache;
      try {
        cache = JSON.parse(content);
        // Bail out if the file or the option changed
        if (!isCacheValid(cache, fileHash, query)) {
          return callback(null);
        }
      } catch (e) {
        return callback(e);
      }
      callback(null, cache.result);
    });
  });
}