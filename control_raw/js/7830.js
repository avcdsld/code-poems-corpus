function getViewSettingsItemByKey(aViewSettingsItems, sKey) {
		var i, oItem;

		// convenience, also allow strings
		// find item with this key
		for (i = 0; i < aViewSettingsItems.length; i++) {
			if (aViewSettingsItems[i].getKey() === sKey) {
				oItem = aViewSettingsItems[i];
				break;
			}
		}

		return oItem;
	}