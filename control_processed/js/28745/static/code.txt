function(plugins) {
    _.each(
      plugins,
      _.bind(function(plugin) {
        if (!this.plugins[plugin]) {
          this.plugins[plugin] = this.requirePlugin(plugin);
        }
      }, this)
    );
  }