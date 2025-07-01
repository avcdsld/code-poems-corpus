function (oControl, sPropertyName, mBindingInfos) {
			var mOldBindingInfos = oControl.getBindingInfo(sPropertyName);
			var vOldValue;

			var oMetadata = oControl.getMetadata().getPropertyLikeSetting(sPropertyName);
			if (oMetadata) {
				var sPropertyGetter = oMetadata._sGetter;
				vOldValue = oControl[sPropertyGetter]();
			}

			JsControlTreeModifier.bindProperty.apply(this, arguments);

			if (mOldBindingInfos){
				this._saveUndoOperation("bindProperty", [oControl, sPropertyName, mOldBindingInfos]);
			} else {
				this._saveUndoOperation("unbindProperty", [oControl, sPropertyName]);
			}
			if (vOldValue) {
				this._saveUndoOperation("setProperty", [oControl, sPropertyName, vOldValue]);
			}
		}