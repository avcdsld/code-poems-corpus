function animate() {
    return function animateImpl(properties, params) {
      var self = this;
      var selfIsArrayLike = self.length !== undefined;
      var all = selfIsArrayLike ? self : [self]; // put in array if not array-like

      var cy = this._private.cy || this;

      if (!cy.styleEnabled()) {
        return this;
      }

      if (params) {
        properties = extend({}, properties, params);
      } // manually hook and run the animation


      for (var i = 0; i < all.length; i++) {
        var ele = all[i];
        var queue = ele.animated() && (properties.queue === undefined || properties.queue);
        var ani = ele.animation(properties, queue ? {
          queue: true
        } : undefined);
        ani.play();
      }

      return this; // chaining
    };
  }