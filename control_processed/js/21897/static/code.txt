function (image) {
            if (!image) {
                throw new ArgumentError(Logger.logMessage(Logger.LEVEL_SEVERE, "ImageSource", "constructor",
                    "missingImage"));
            }

            /**
             * This image source's image
             * @type {Image}
             * @readonly
             */
            this.image = image;

            /**
             * This image source's key. A unique key is automatically generated and assigned during construction.
             * Applications may assign a different key after construction.
             * @type {String}
             * @default A unique string for this image source.
             */
            this.key = "ImageSource " + ++ImageSource.keyPool;
        }