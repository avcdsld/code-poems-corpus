function next(bFound) {
			if (bFound) {
				return aElements[i];
			}
			i += 1;
			if (i < aElements.length) {
				return fnCallback(aElements[i], i, aElements).then(next);
			}
		}