function (value) {
                if (this._intersectionThreshold === value) {
                    return;
                }
                this._intersectionThreshold = value;
                if (this.geometry) {
                    this.geometry.boundingBias = new BABYLON.Vector2(0, value);
                }
            }