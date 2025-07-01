function(sName) {
			if (this._oDimensionSet[sName]) { // the easy case
				return this._oDimensionSet[sName];
			}

			for ( var sDimensionName in this._oDimensionSet) {
				var oDimension = this._oDimensionSet[sDimensionName];
				var oTextProperty = oDimension.getTextProperty();
				if (oTextProperty && oTextProperty.name == sName) {
					return oDimension;
				}
				if (oDimension.findAttributeByName(sName)) {
					return oDimension;
				}
			}
			return null;
		}