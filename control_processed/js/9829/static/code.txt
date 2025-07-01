function findRegisteredFontSet(alias) {
    var useDefault = angular.isUndefined(alias) || !(alias && alias.length);
    if (useDefault) {
      return config.defaultFontSet;
    }

    var result = alias;
    angular.forEach(config.fontSets, function(fontSet) {
      if (fontSet.alias === alias) {
        result = fontSet.fontSet || result;
      }
    });

    return result;
  }