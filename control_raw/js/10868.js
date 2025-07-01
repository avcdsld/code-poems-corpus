function MegaPixImage(srcImage, errorCallback) {
        var self = this;

        if (window.Blob && srcImage instanceof Blob) {
            (function() {
                var img = new Image(),
                    URL = window.URL && window.URL.createObjectURL ? window.URL :
                        window.webkitURL && window.webkitURL.createObjectURL ? window.webkitURL : null;
                if (!URL) { throw Error("No createObjectURL function found to create blob url"); }
                img.src = URL.createObjectURL(srcImage);
                self.blob = srcImage;
                srcImage = img;
            }());
        }
        if (!srcImage.naturalWidth && !srcImage.naturalHeight) {
            srcImage.onload = function() {
                var listeners = self.imageLoadListeners;
                if (listeners) {
                    self.imageLoadListeners = null;
                    // IE11 doesn't reliably report actual image dimensions immediately after onload for small files,
                    // so let's push this to the end of the UI thread queue.
                    setTimeout(function() {
                        for (var i = 0, len = listeners.length; i < len; i++) {
                            listeners[i]();
                        }
                    }, 0);
                }
            };
            srcImage.onerror = errorCallback;
            this.imageLoadListeners = [];
        }
        this.srcImage = srcImage;
    }