function (sector, level, row, column, cacheKey) {
            if (!cacheKey || (cacheKey.length < 1)) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "FramebufferTile", "constructor",
                        "The specified cache name is null, undefined or zero length."));
            }

            TextureTile.call(this, sector, level, row, column); // args are checked in the superclass' constructor

            // Assign the cacheKey as the gpuCacheKey (inherited from TextureTile).
            this.gpuCacheKey = cacheKey;

            // Internal. Intentionally not documented.
            this.textureTransform = Matrix.fromIdentity().setToUnitYFlip();

            // Internal. Intentionally not documented.
            this.mustClear = true;
        }