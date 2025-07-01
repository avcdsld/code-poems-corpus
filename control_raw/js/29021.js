function() {
        var self = this;

        var request = this._createRequest();

        return request.then(function(response) {
          //update sid for next querying.
          if (response.sid) {
            self._oldSid = self._sid;
            self._sid = response.sid;
          } else {
            self._sid = null;
            self._hitEnd = true;
          }
          self._hits = response.hits || 0;

          return _.map(response.results, function(json) {
            if (json.className) {
              response.className = json.className;
            }
            var obj = self._newObject(response);
            obj.appURL = json['_app_url'];
            obj._finishFetch(self._processResult(json), true);
            return obj;
          });
        });
      }