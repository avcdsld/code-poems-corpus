function filterDuplicates(/*ref*/ aMessages){
		if (aMessages.length > 1) {
			for (var iIndex = 1; iIndex < aMessages.length; iIndex++) {
				if (aMessages[0].getCode() == aMessages[iIndex].getCode() && aMessages[0].getMessage() == aMessages[iIndex].getMessage()) {
					aMessages.shift(); // Remove outer error, since inner error is more detailed
					break;
				}
			}
		}
	}