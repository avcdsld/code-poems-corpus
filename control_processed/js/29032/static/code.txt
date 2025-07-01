function(key) {
        var self = this;
        delete this.attributes[key];
        if (this._serverData[key]) {
          this.attributes[key] = this._serverData[key];
        }
        AV._arrayEach(this._opSetQueue, function(opSet) {
          var op = opSet[key];
          if (op) {
            const [value, actualTarget, actualKey, firstKey] = findValue(
              self.attributes,
              key
            );
            setValue(self.attributes, key, op._estimate(value, self, key));
            if (actualTarget && actualTarget[actualKey] === AV.Op._UNSET) {
              delete actualTarget[actualKey];
            }
            self._resetCacheForKey(firstKey);
          }
        });
      }