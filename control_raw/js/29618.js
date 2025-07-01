function(onDone) {
			var result = Array.isArray(this._selections) ? this._selections.slice() : [];
			if (typeof onDone === "function") { //$NON-NLS-0$
				onDone(result);
			}
			return result;
		}