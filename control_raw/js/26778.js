function unpackMethodSets(methods) {
    var result = [];

    methods.forEach(function(method) {
      if (method.set) {
        method.set.forEach(function(name) {
          var setMethod = clone(method);
          setMethod.name = name;
          result.push(setMethod);
        });
      } else {
        result.push(method);
      }
    });
    return result;
  }