function _setDateInDatesRow(oDate) {

		var oDatesRow = this.getAggregation("datesRow");
		var oHeader = this.getAggregation("header");

		if (!this.getPickerPopup()) {
			// set number of days - but max number of days of this month
			var oLastDayOfMonth = new UniversalDate(oDate.getTime());
			oLastDayOfMonth.setUTCDate(1);
			oLastDayOfMonth.setUTCMonth(oLastDayOfMonth.getUTCMonth() + 1);
			oLastDayOfMonth.setUTCDate(0);
			var iDays = oDatesRow.getDays();

			// set start day and selected day
			var oStartDate = new UniversalDate(oDate.getTime());
			oStartDate.setUTCDate( 1 + (Math.ceil(oDate.getUTCDate() / iDays) - 1) * iDays );
			if (oLastDayOfMonth.getUTCDate() - oStartDate.getUTCDate() < iDays) {
				oStartDate.setUTCDate(oLastDayOfMonth.getUTCDate() - iDays + 1);
			}

			oDatesRow.setStartDate(CalendarUtils._createLocalDate(oStartDate, true));

			var iYear = oStartDate.getJSDate().getUTCFullYear();
			var iYearMax = this._oMaxDate.getJSDate().getUTCFullYear();
			var iYearMin = this._oMinDate.getJSDate().getUTCFullYear();
			var iMonth = oStartDate.getJSDate().getUTCMonth();
			var iMonthMax = this._oMaxDate.getJSDate().getUTCMonth();
			var iMonthMin = this._oMinDate.getJSDate().getUTCMonth();
			var iDate = oStartDate.getJSDate().getUTCDate();
			var iDateMax = this._oMaxDate.getJSDate().getUTCDate();
			var iDateMin = this._oMinDate.getJSDate().getUTCDate();

			if (iDate <= 1 || (iYear == iYearMin && iMonth == iMonthMin && iDate <= iDateMin)) {
				oHeader.setEnabledPrevious(false);
			} else {
				oHeader.setEnabledPrevious(true);
			}

			if ((iDate + iDays) >= oLastDayOfMonth.getUTCDate() || (iYear == iYearMax && iMonth == iMonthMax && iDate >= iDateMax)) {
				oHeader.setEnabledNext(false);
			} else {
				oHeader.setEnabledNext(true);
			}
		} else {
			oHeader.setEnabledPrevious(false);
			oHeader.setEnabledNext(false);
		}

		oDatesRow.setDate(CalendarUtils._createLocalDate(oDate, true));
	}