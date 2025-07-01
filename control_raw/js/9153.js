function updateSingleArray(aOrig, aAdditional, bRemove) {
		if (!aAdditional) {
			return;
		}

		for (var i = 0; i < aAdditional.length; i++) {
			var iIndex = aOrig.indexOf(aAdditional[i]);
			if (iIndex > -1 && bRemove) {
				aOrig.splice(iIndex, 1);
			} else if (iIndex === -1 && !bRemove) {
				aOrig.push(aAdditional[i]);
			}
		}
	}