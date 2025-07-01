function(array, without, property) {
      return _.filter(Array.isArray(array) ? array : [], function(item) {
        return !_.find(without || [], function(other) {
          if (property) {
            return _.isEqual(item[property], other);
          } else {
            return _.isEqual(item, other);
          }
        });
      });
    }