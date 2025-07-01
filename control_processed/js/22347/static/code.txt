function( viewportZoom ) {
        var ratio = this._scaleSpring.current.value *
                this.viewport._containerInnerSize.x / this.source.dimensions.x;
        return ratio * viewportZoom;
    }