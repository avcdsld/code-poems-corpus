function _removeSubPropAliases(layer) {
	var propName;
	for (propName in layer) {
		if (Object.prototype.hasOwnProperty.call(layer, propName)) {
			if (propName.indexOf('.') !== -1) {
				delete layer[propName];
			}
		}
	}
}