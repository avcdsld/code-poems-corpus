function () {
				EventProvider.prototype.destroy.apply(this);

				this._aPattern = null;
				this._aRoutes = null;
				this._oParent = null;
				this._oConfig = null;

				this.bIsDestroyed = true;

				return this;
			}