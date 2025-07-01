function(sDimensionName, bIncludeKey, bIncludeText, aAttributeName) {
			this._oSelectedPropertyNames = null; // reset previously compiled list of selected properties

			var aDimName = [];
			if (sDimensionName) {
				if (this._oAggregationLevel[sDimensionName] == undefined) {
					throw sDimensionName + " is not included in the aggregation level";
				}
				aDimName.push(sDimensionName);
			} else {
				for ( var sName in this._oAggregationLevel) {
					aDimName.push(sName);
				}
				aAttributeName = null;
			}
			for (var i = -1, sDimName; (sDimName = aDimName[++i]) !== undefined;) {
				if (bIncludeKey != null) {
					this._oAggregationLevel[sDimName].key = bIncludeKey;
				}
				if (bIncludeText != null) {
					this._oAggregationLevel[sDimName].text = bIncludeText;
				}
				if (aAttributeName != null) {
					this._oAggregationLevel[sDimName].attributes = aAttributeName;
				}
			}
		}