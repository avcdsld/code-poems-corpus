function (sector, imageSource) {
            if (!sector) {
                throw new ArgumentError(Logger.logMessage(Logger.LEVEL_SEVERE, "SurfaceImage", "constructor",
                    "missingSector"));
            }

            if (!imageSource) {
                throw new ArgumentError(Logger.logMessage(Logger.LEVEL_SEVERE, "SurfaceImage", "constructor",
                    "missingImage"));
            }

            SurfaceTile.call(this, sector);

            /**
             * Indicates whether this surface image is drawn.
             * @type {boolean}
             * @default true
             */
            this.enabled = true;

            /**
             * The path to the image.
             * @type {String}
             */
            this._imageSource = imageSource;

            /**
             * This surface image's resampling mode. Indicates the sampling algorithm used to display this image when it
             * is larger on screen than its native resolution. May be one of:
             * <ul>
             *  <li>WorldWind.FILTER_LINEAR</li>
             *  <li>WorldWind.FILTER_NEAREST</li>
             * </ul>
             * @default WorldWind.FILTER_LINEAR
             */
            this.resamplingMode = WorldWind.FILTER_LINEAR;

            /**
             * This surface image's opacity. When this surface image is drawn, the actual opacity is the product of
             * this opacity and the opacity of the layer containing this surface image.
             * @type {number}
             */
            this.opacity = 1;

            /**
             * This surface image's display name;
             * @type {string}
             */
            this.displayName = "Surface Image";

            // Internal. Indicates whether the image needs to be updated in the GPU resource cache.
            this.imageSourceWasUpdated = true;
        }