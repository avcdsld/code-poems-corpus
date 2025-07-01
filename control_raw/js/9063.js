function() {
			clearTimeout(this._delayedCallId);

			// if interval is active and there are registered listeners
			var bHasListeners = this._oEventBus._defaultChannel.hasListeners(_EVENT_ID);
			if (this._iInterval > 0 && bHasListeners) {
				this._oEventBus.publish(_EVENT_ID);

				this._delayedCallId = setTimeout(this._trigger, this._iInterval);
			}
		}