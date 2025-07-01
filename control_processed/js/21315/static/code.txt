function lookupWrapper(objectType, lookupFunction) {
  lookupFunction = lookupFunction || objectType.lookup;

  return function(repo, id, callback) {
    if (id instanceof objectType) {
      return Promise.resolve(id).then(function(obj) {
        obj.repo = repo;

        if (typeof callback === "function") {
          callback(null, obj);
        }

        return obj;
      }, callback);
    }

    return lookupFunction(repo, id).then(function(obj) {
      obj.repo = repo;

      if (typeof callback === "function") {
        callback(null, obj);
      }

      return obj;
    }, callback);
  };
}