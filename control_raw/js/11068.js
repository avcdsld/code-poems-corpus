function(list, property) {
      if (_.isArray(list)) {
        return _.some(list, function(item) { return _.has(item, property); });
      } else {
        return _.has(list, property);
      }
    }