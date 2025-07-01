function (oEvent) {
			var iPageY = oEvent.changedTouches && oEvent.changedTouches.length ? oEvent.changedTouches[0].pageY : oEvent.pageY;

			if (this._bIsDrag === false) {
				this.fireTap(oEvent);
				this._dragSession = null;
			}

			this._bIsDrag = true;

			if (!this.getIsExpanded()) {
				this._dragSession = null;
				return;
			}

			this._endDrag(iPageY, oEvent.timeStamp);

			this._mousedown = false;
		}