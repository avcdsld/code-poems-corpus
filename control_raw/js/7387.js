function() {
			if (this._aHierarchyPropertyNames) {
				return this._aHierarchyPropertyNames;
			}

			this._aHierarchyPropertyNames = [];

			for ( var sName in this._oRecursiveHierarchySet) {
				this._aHierarchyPropertyNames.push(this._oRecursiveHierarchySet[sName].getNodeValueProperty().name);
			}

			return this._aHierarchyPropertyNames;
		}