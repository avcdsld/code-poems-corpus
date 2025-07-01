function () {
            var levels = [{
                    url: this._image.src,
                    /* IE8 fix since it has no naturalWidth and naturalHeight */
                    width: Object.prototype.hasOwnProperty.call(this._image, 'naturalWidth') ? this._image.naturalWidth : this._image.width,
                    height:  Object.prototype.hasOwnProperty.call(this._image, 'naturalHeight') ? this._image.naturalHeight : this._image.height
                }];

            if (!this.buildPyramid || !$.supportsCanvas || !this.useCanvas) {
                // We don't need the image anymore. Allows it to be GC.
                delete this._image;
                return levels;
            }

            /* IE8 fix since it has no naturalWidth and naturalHeight */
            var currentWidth = Object.prototype.hasOwnProperty.call(this._image, 'naturalWidth') ? this._image.naturalWidth : this._image.width;
            var currentHeight = Object.prototype.hasOwnProperty.call(this._image, 'naturalHeight') ? this._image.naturalHeight : this._image.height;


            var bigCanvas = document.createElement("canvas");
            var bigContext = bigCanvas.getContext("2d");

            bigCanvas.width = currentWidth;
            bigCanvas.height = currentHeight;
            bigContext.drawImage(this._image, 0, 0, currentWidth, currentHeight);
            // We cache the context of the highest level because the browser
            // is a lot faster at downsampling something it already has
            // downsampled before.
            levels[0].context2D = bigContext;
            // We don't need the image anymore. Allows it to be GC.
            delete this._image;

            if ($.isCanvasTainted(bigCanvas)) {
                // If the canvas is tainted, we can't compute the pyramid.
                return levels;
            }

            // We build smaller levels until either width or height becomes
            // 1 pixel wide.
            while (currentWidth >= 2 && currentHeight >= 2) {
                currentWidth = Math.floor(currentWidth / 2);
                currentHeight = Math.floor(currentHeight / 2);
                var smallCanvas = document.createElement("canvas");
                var smallContext = smallCanvas.getContext("2d");
                smallCanvas.width = currentWidth;
                smallCanvas.height = currentHeight;
                smallContext.drawImage(bigCanvas, 0, 0, currentWidth, currentHeight);

                levels.splice(0, 0, {
                    context2D: smallContext,
                    width: currentWidth,
                    height: currentHeight
                });

                bigCanvas = smallCanvas;
                bigContext = smallContext;
            }
            return levels;
        }