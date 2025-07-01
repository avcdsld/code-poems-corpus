function(options) {
        options = options || {};
        options.unset = true;
        var keysToClear = _.extend(this.attributes, this._operations);
        return this.set(keysToClear, options);
      }