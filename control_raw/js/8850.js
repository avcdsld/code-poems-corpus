function _renderTimesRow(bSkipFocus){

		var oDate = this._getFocusedDate();
		var oTimesRow = this.getAggregation("timesRow");

		if (!bSkipFocus) {
			oTimesRow.setDate(CalendarUtils._createLocalDate(oDate, true));
		} else {
			oTimesRow.displayDate(CalendarUtils._createLocalDate(oDate, true));
		}

		// change header buttons
		_updateHeader.call(this);

	}