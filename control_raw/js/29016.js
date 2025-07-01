function(keys) {
        requires(keys, 'undefined is not a valid key');
        _(arguments).forEach(keys => {
          this._include = this._include.concat(ensureArray(keys));
        });
        return this;
      }