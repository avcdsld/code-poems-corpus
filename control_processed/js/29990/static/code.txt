function resolve(thing, neverForceAsync) {
  if (forceAsync && !neverForceAsync) {
    var deferred = Promise.defer();
    setTimeout(function() {
      Promise.resolve(thing).then(function(resolved) {
        if (typeof resolved === 'function') {
          resolved = resolve(resolved(), neverForceAsync);
        }

        deferred.resolve(resolved);
      });
    }, 500);
    return deferred.promise;
  }

  return Promise.resolve(thing).then(function(resolved) {
    if (typeof resolved === 'function') {
      return resolve(resolved(), neverForceAsync);
    }
    return resolved;
  });
}