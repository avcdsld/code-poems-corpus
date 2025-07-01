function(oEvent){
		jQuery(document.body).unbind("selectstart." + this.getId()).unbind("mouseup." + this.getId()).unbind("mousemove." + this.getId());
		this.$("ghost").remove();
		this.$("rsz").removeClass("sapUiUx3ExactLstRSzDrag");
		this._iStartWidth = undefined;
		this._iStartDragX = undefined;
		this.focus();
	}