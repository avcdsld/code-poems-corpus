function (url, callback, options) {
      return fabric.util.loadImage(url, function(img) {
        this.backgroundImage = img;
        if (options && ('backgroundImageOpacity' in options)) {
            this.backgroundImageOpacity = options.backgroundImageOpacity;
        }
        if (options && ('backgroundImageStretch' in options)) {
            this.backgroundImageStretch = options.backgroundImageStretch;
        }
        callback && callback();
      }, this);
    }