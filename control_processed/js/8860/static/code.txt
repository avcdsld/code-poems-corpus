function _handleSelectYear(oEvent){

		var oFocusedDate = new UniversalDate(this._getFocusedDate().getTime());
		var oYearPicker = this.getAggregation("yearPicker");
		var oDate = CalendarUtils._createUniversalUTCDate(oYearPicker.getDate());
		var iMonth = oFocusedDate.getUTCMonth();

		oDate.setUTCMonth(oFocusedDate.getUTCMonth(), oFocusedDate.getUTCDate()); // to keep day and month stable also for islamic date
		oDate.setUTCHours(oFocusedDate.getUTCHours());
		oDate.setUTCMinutes(oFocusedDate.getUTCMinutes());
		oFocusedDate = oDate;

		if (iMonth != oFocusedDate.getUTCMonth() ) {
			// day did not exist in this year (29. Feb) -> go to last day of month
			oFocusedDate.setUTCDate(0);
		}

		_focusDate.call(this, oFocusedDate, true);

		_hideYearPicker.call(this);

	}