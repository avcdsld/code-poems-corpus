function() {
			var iEnd = null;
			if (this._iTopRequestOption != null) {
				if (this._iSkipRequestOption == null) {
					iEnd = 1;
				} else {
					iEnd = this._iSkipRequestOption + this._iTopRequestOption;
				}
			}
			return {
				start : (this._iSkipRequestOption == null) ? 1 : this._iSkipRequestOption,
				end : iEnd
			};
		}