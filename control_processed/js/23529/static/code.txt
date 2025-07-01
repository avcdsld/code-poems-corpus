function() {

      var NUM_FRACTION_DIGITS = fabric.Object.NUM_FRACTION_DIGITS;

      var object = {
        type:             this.type,
        left:             toFixed(this.left, NUM_FRACTION_DIGITS),
        top:              toFixed(this.top, NUM_FRACTION_DIGITS),
        width:            toFixed(this.width, NUM_FRACTION_DIGITS),
        height:           toFixed(this.height, NUM_FRACTION_DIGITS),
        fill:             (this.fill && this.fill.toObject) ? this.fill.toObject() : this.fill,
        overlayFill:      this.overlayFill,
        stroke:           this.stroke,
        strokeWidth:      this.strokeWidth,
        strokeDashArray:  this.strokeDashArray,
        scaleX:           toFixed(this.scaleX, NUM_FRACTION_DIGITS),
        scaleY:           toFixed(this.scaleY, NUM_FRACTION_DIGITS),
        angle:            toFixed(this.getAngle(), NUM_FRACTION_DIGITS),
        flipX:            this.flipX,
        flipY:            this.flipY,
        opacity:          toFixed(this.opacity, NUM_FRACTION_DIGITS),
        selectable:       this.selectable,
        hasControls:      this.hasControls,
        hasBorders:       this.hasBorders,
        hasRotatingPoint: this.hasRotatingPoint,
        transparentCorners: this.transparentCorners,
        perPixelTargetFind: this.perPixelTargetFind
      };

      if (!this.includeDefaultValues) {
        object = this._removeDefaultValues(object);
      }

      return object;
    }