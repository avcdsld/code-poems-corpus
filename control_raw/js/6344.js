function style$$1(name, value) {
    var cy = this.cy();

    if (!cy.styleEnabled()) {
      return this;
    }

    var updateTransitions = false;
    var style$$1 = cy.style();

    if (plainObject(name)) {
      // then extend the bypass
      var props = name;
      style$$1.applyBypass(this, props, updateTransitions);
      this.emitAndNotify('style'); // let the renderer know we've updated style
    } else if (string(name)) {
      if (value === undefined) {
        // then get the property from the style
        var ele = this[0];

        if (ele) {
          return style$$1.getStylePropertyValue(ele, name);
        } else {
          // empty collection => can't get any value
          return;
        }
      } else {
        // then set the bypass with the property value
        style$$1.applyBypass(this, name, value, updateTransitions);
        this.emitAndNotify('style'); // let the renderer know we've updated style
      }
    } else if (name === undefined) {
      var _ele = this[0];

      if (_ele) {
        return style$$1.getRawStyle(_ele);
      } else {
        // empty collection => can't get any value
        return;
      }
    }

    return this; // chaining
  }