function(serverData, hasData) {
        // Clear out any changes the user might have made previously.
        this._opSetQueue = [{}];

        // Bring in all the new server data.
        this._mergeMagicFields(serverData);
        var self = this;
        AV._objectEach(serverData, function(value, key) {
          self._serverData[key] = AV._decode(value, key);
        });

        // Refresh the attributes.
        this._rebuildAllEstimatedData();

        // Clear out the cache of mutable containers.
        this._refreshCache();
        this._opSetQueue = [{}];

        this._hasData = hasData;
      }