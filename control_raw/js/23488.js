function (url, callback) { // TODO (kangax): test callback
      fabric.util.loadImage(url, function(img) {
        this.overlayImage = img;
        callback && callback();
      }, this);
      return this;
    }