function(current) {
        var bounds = this.getBoundsNoRotate(current);
        if (this._clip) {
            var worldWidth = current ?
                this._worldWidthCurrent : this._worldWidthTarget;
            var ratio = worldWidth / this.source.dimensions.x;
            var clip = this._clip.times(ratio);
            bounds = new $.Rect(
                bounds.x + clip.x,
                bounds.y + clip.y,
                clip.width,
                clip.height);
        }
        return bounds.rotate(this.getRotation(current), this._getRotationPoint(current));
    }