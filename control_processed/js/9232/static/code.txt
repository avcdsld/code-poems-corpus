function () {
				if (this.bIsDestroyed) {
					return this;
				}

				EventProvider.prototype.destroy.apply(this);

				// destroy the view cache
				if (this._oViews) {
					this._oViews.destroy();
					this._oViews = null;
				}

				if (!this._bIsInitialized) {
					Log.info("Router is not initialized, but got destroyed.", this);
				}

				if (this.fnHashChanged) {
					this.oHashChanger.detachEvent("hashChanged", this.fnHashChanged);
				}

				if (this.fnHashReplaced) {
					this.oHashChanger.detachEvent("hashReplaced", this.fnHashReplaced);
				}

				//will remove all the signals attached to the routes - all the routes will not be useable anymore
				this._oRouter.removeAllRoutes();
				this._oRouter = null;

				jQuery.each(this._oRoutes, function(iRouteIndex, oRoute) {
					oRoute.destroy();
				});
				this._oRoutes = null;
				this._oConfig = null;

				if (this._oTargets) {
					this._oTargets.destroy();
					this._oTargets = null;
				}

				delete this._bIsInitialized;
				this.bIsDestroyed = true;

				return this;
			}