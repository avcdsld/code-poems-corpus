function(sPropertyName) {
			var oProperty = this._oPropertySet[sPropertyName];
			if (oProperty == null) {
				throw "no such property with name " + sPropertyName;
			}

			if (oProperty.extensions != undefined) {
				for (var i = -1, oExtension; (oExtension = oProperty.extensions[++i]) !== undefined;) {
					if (oExtension.name == "text") {
						return this.findPropertyByName(oExtension.value);
					}
				}
			}
			return null;
		}