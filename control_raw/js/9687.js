function getSize(value) {
    var defaultValue = $mdProgressCircular.progressSize;

    if (value) {
      var parsed = parseFloat(value);

      if (value.lastIndexOf('%') === value.length - 1) {
        parsed = (parsed / 100) * defaultValue;
      }

      return parsed;
    }

    return defaultValue;
  }