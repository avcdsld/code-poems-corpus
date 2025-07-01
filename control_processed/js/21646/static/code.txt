function(width, height, animate) {

		if (width) {
			this.options.width = width;
		}
		if (height && height != this.options.height) {
			this.options.height = height;
			this.timescale = this._getTimeScale();
		}

		// Size Markers
		this._assignRowsToMarkers();

		// Size swipable area
		this._el.slider_background.style.width = this.timescale.getPixelWidth() + this.options.width + "px";
		this._el.slider_background.style.left = -(this.options.width/2) + "px";
		this._el.slider.style.width = this.timescale.getPixelWidth() + this.options.width + "px";

		// Update Swipable constraint
		this._swipable.updateConstraint({top: false,bottom: false,left: (this.options.width/2),right: -(this.timescale.getPixelWidth() - (this.options.width/2))});

		// Go to the current slide
		this.goToId(this.current_id, true);
	}