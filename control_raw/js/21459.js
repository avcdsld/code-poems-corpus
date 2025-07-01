function (object /* args */) {
    var methods = [].slice.call(arguments, 1);
    if (arguments.length === 2 && Array.isArray(arguments[1])) {
      methods = arguments[1];
    }

    methods.forEach(function (method) {
      if (typeof object[method] === 'function') {
        object[method] = object[method].bind(object);
      }
    });

    return object;
  }