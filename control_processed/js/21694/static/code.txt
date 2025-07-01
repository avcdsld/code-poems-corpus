function () {
		
		// Create Layout
		this._el.message_container = TL.Dom.create("div", "tl-message-container", this._el.container);
		this._el.loading_icon = TL.Dom.create("div", this.options.message_icon_class, this._el.message_container);
		this._el.message = TL.Dom.create("div", "tl-message-content", this._el.message_container);
		
		this._updateMessage();
		
	}