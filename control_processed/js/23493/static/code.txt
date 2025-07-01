function () {
      this._objects.push.apply(this._objects, arguments);
      for (var i = arguments.length; i--; ) {
        this._initObject(arguments[i]);
      }
      this.renderOnAddition && this.renderAll();
      return this;
    }