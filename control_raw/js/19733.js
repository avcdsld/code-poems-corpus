function Angle(radians) {
            var _this = this;
            /**
             * Returns the Angle value in degrees (float).
             */
            this.degrees = function () { return _this._radians * 180.0 / Math.PI; };
            /**
             * Returns the Angle value in radians (float).
             */
            this.radians = function () { return _this._radians; };
            this._radians = radians;
            if (this._radians < 0.0)
                this._radians += (2.0 * Math.PI);
        }