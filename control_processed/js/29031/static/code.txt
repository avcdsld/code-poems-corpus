function(key) {
        var value = this.attributes[key];
        if (
          _.isObject(value) &&
          !(value instanceof AV.Object) &&
          !(value instanceof AV.File)
        ) {
          var json = JSON.stringify(recursiveToPointer(value));
          if (this._hashedJSON[key] !== json) {
            var wasSet = !!this._hashedJSON[key];
            this._hashedJSON[key] = json;
            return wasSet;
          }
        }
        return false;
      }