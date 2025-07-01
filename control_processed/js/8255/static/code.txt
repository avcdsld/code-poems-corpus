function deleteMetadataForEntry(self, key) {
			var iIndex = self._metadata.__byKey__[key];
			delete self._metadata.__byKey__[key];
			delete self._metadata.__byIndex__[iIndex];
			seekMetadataLRU(self);
		}