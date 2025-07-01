function(options) {
        var params = {
          skip: this._skip,
          limit: this._limit,
        };

        return request({
          path: `/bigquery/jobs/${this.id}`,
          method: 'GET',
          query: params,
          authOptions: options,
          signKey: false,
        }).then(function(response) {
          if (response.error) {
            return Promise.reject(new AVError(response.code, response.error));
          }
          return Promise.resolve(response);
        });
      }