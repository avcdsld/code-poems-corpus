function () {
			var oModel = this._oDialog.getModel("view"),
				sSelectedLocation = oModel.getProperty("/SelectedLocation"),
				oControl;

			if (sSelectedLocation === "custom") {
				oControl = this._getControl("customBootstrapURL",this._SUPPORT_ASSISTANT_POPOVER_ID);
				var sValue = oControl.getValue();
				try {
					this._validateValue(sValue);
				} catch (oException) {
					this._showError(oControl, oException.message);
					if (this._sErrorMessage) {
						this._sErrorMessage = null;
					}
					return;
				}
			} else {
				oControl = this._getControl("standardBootstrapURL", this._SUPPORT_ASSISTANT_POPOVER_ID);
			}

			if (this._sErrorMessage) {
				this._showError(oControl, this._sErrorMessage);
				this._sErrorMessage = null;
			}
		}