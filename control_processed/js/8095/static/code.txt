function (mChangeListeners, sPropertyPath, vValue) {
			var aListeners = mChangeListeners[sPropertyPath],
				i;

			if (aListeners) {
				for (i = 0; i < aListeners.length; i += 1) {
					aListeners[i].onChange(vValue);
				}
			}
		}