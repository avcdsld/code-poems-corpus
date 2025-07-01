function _fieldsChanged(oChanges) {

			if (oChanges.child) {
				_fieldChanged.call(this, oChanges.child, oChanges.mutation);
			} else if (oChanges.children) {
				for (var i = 0; i < oChanges.chlidren.length; i++) {
					_fieldChanged.call(this, oChanges.children[i], oChanges.mutation);
				}
			}

		_updateLabelFor.call(this);

	}