function (position, attributes) {

            if (!position) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "Annotation", "constructor", "missingPosition"));
            }

            Renderable.call(this);

            /**
             * This annotation's geographic position.
             * @type {Position}
             */
            this.position = position;

            /**
             * The annotation's attributes.
             * @type {AnnotationAttributes}
             * @default see [AnnotationAttributes]{@link AnnotationAttributes}
             */
            this.attributes = attributes ? attributes : new AnnotationAttributes(null);

            /**
             * This annotation's altitude mode. May be one of
             * <ul>
             *  <li>[WorldWind.ABSOLUTE]{@link WorldWind#ABSOLUTE}</li>
             *  <li>[WorldWind.RELATIVE_TO_GROUND]{@link WorldWind#RELATIVE_TO_GROUND}</li>
             *  <li>[WorldWind.CLAMP_TO_GROUND]{@link WorldWind#CLAMP_TO_GROUND}</li>
             * </ul>
             * @default WorldWind.ABSOLUTE
             */
            this.altitudeMode = WorldWind.ABSOLUTE;

            // Internal use only. Intentionally not documented.
            this.layer = null;

            // Internal use only. Intentionally not documented.
            this.lastStateKey = null;

            // Internal use only. Intentionally not documented.
            this.calloutTransform = Matrix.fromIdentity();

            // Internal use only. Intentionally not documented.
            this.calloutOffset = new WorldWind.Offset(
                WorldWind.OFFSET_FRACTION, 0.5,
                WorldWind.OFFSET_FRACTION, 0);

            // Internal use only. Intentionally not documented.
            this.label = "";

            // Internal use only. Intentionally not documented.
            this.labelTexture = null;

            // Internal use only. Intentionally not documented.
            this.labelTransform = Matrix.fromIdentity();

            // Internal use only. Intentionally not documented.
            this.placePoint = new Vec3(0, 0, 0);

            // Internal use only. Intentionally not documented.
            this.depthOffset = -2.05;

            // Internal use only. Intentionally not documented.
            this.calloutPoints = null;
        }