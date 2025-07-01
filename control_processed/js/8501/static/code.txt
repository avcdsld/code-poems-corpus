function alignPreprocessorStructure(oPreprocessor) {
		oPreprocessor._settings = {};
		for (var sProp in oPreprocessor) {
			// copy all relevant settings to the internal settings object which gets passed to the preprocessor function
			if (sProp.indexOf("_") !== 0) {
				oPreprocessor._settings[sProp] = oPreprocessor[sProp];
			}
		}
	}