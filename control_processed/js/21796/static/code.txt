function (worldWindow) {
            if (!worldWindow) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "FrameStatisticsLayer", "constructor", "missingWorldWindow"));
            }

            Layer.call(this, "Frame Statistics");

            // No picking of this layer's screen elements.
            this.pickEnabled = false;

            var textAttributes = new TextAttributes(null);
            textAttributes.color = Color.GREEN;
            textAttributes.font = new Font(12);
            textAttributes.offset = new Offset(WorldWind.OFFSET_FRACTION, 0, WorldWind.OFFSET_FRACTION, 1);

            // Intentionally not documented.
            this.frameTime = new ScreenText(new Offset(WorldWind.OFFSET_PIXELS, 5, WorldWind.OFFSET_INSET_PIXELS, 5), " ");
            this.frameTime.attributes = textAttributes;

            // Intentionally not documented.
            this.frameRate = new ScreenText(new Offset(WorldWind.OFFSET_PIXELS, 5, WorldWind.OFFSET_INSET_PIXELS, 25), " ");
            this.frameRate.attributes = textAttributes;

            // Register a redraw callback on the WorldWindow.
            var thisLayer = this;

            function redrawCallback(worldWindow, stage) {
                thisLayer.handleRedraw(worldWindow, stage);
            }

            worldWindow.redrawCallbacks.push(redrawCallback);
        }