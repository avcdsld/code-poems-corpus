function (coord, clamp) {
        var extent = this._extent;
        var scale = this.scale;

        if (this.onBand && scale.type === 'ordinal') {
            extent = extent.slice();
            fixExtentWithBands(extent, scale.count());
        }

        var t = linearMap(coord, extent, NORMALIZED_EXTENT, clamp);

        return this.scale.scale(t);
    }