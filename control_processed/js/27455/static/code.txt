function mapValidation (results) {
  var res = {};

  normalizeMap(results).forEach(function (ref) {
    var key = ref.key;
    var val = ref.val;

    res[key] = function mappedValidation () {
      var validation = this.$validation;
      if (!this._isMounted) {
        return null
      }
      var paths = val.split('.');
      var first = paths.shift();
      if (first !== '$validation') {
        warn(("unknown validation result path: " + val));
        return null
      }
      var path;
      var value = validation;
      do {
        path = paths.shift();
        value = value[path];
      } while (paths.length > 0 && value !== undefined)
      return value
    };
  });

  return res
}