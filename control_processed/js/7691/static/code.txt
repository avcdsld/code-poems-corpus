function _updateLabelFor(){
		var aFields = this.getFields();
		var oField = aFields.length > 0 ? aFields[0] : null;

		var oLabel = this._oLabel;
		if (oLabel) {
			oLabel.setLabelFor(oField); // as Label is internal of FormElement, we can use original labelFor
		} else {
			oLabel = this.getLabel();
			if (oLabel instanceof Control /*might also be a string*/) {
				oLabel.setAlternativeLabelFor(oField);
			}
		}
	}