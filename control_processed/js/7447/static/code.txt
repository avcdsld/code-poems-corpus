function(oData) {
			if (this._oModel) {
				this._oModel.destroy();
				delete this._oModel;
			}
			if (oData) {
				this._oModel = new JSONModel(oData);
				this._getTable().setModel(this._oModel);
			} else {
				this._getTable().setModel(null);
			}
			this.setProperty("data", oData);
		}