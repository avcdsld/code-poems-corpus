function (oParent, sName, oObject, iIndex) {
			var oOldAggregationValue = JsControlTreeModifier.getAggregation.call(this, oParent, sName);

			JsControlTreeModifier.insertAggregation.apply(this, arguments);

			if (oParent) {
				if (oParent.getMetadata) {
					var oMetadata = oParent.getMetadata();
					var oAggregations = oMetadata.getAllAggregations();
					if (oAggregations) {
						var oAggregation = oAggregations[sName];
						if (oAggregation) {
							if (oAggregation.multiple) {
								this._saveUndoOperation("removeAggregation", [oParent, sName, oObject]);
							} else {
								this._saveUndoOperation("insertAggregation", [oParent, sName, oOldAggregationValue]);
							}
						}
					}
				}
			}
		}