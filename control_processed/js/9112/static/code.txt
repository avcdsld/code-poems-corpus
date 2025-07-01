function toGregorian(oIslamic) {
		var iIslamicYear = oIslamic.year,
			iIslamicMonth = oIslamic.month,
			iIslamicDate = oIslamic.day,
		/* Islamic Calendar starts from  0001/0/1 (19 July 622 AD), so for any date before it customization is not needed */
			iMonthStart = iIslamicYear < 1 ? monthStart(iIslamicYear, iIslamicMonth) : getCustomMonthStartDays(12 * (iIslamicYear - 1) + iIslamicMonth),
			iJulianDay = iIslamicDate + iMonthStart + ISLAMIC_EPOCH_DAYS - 1,
			iJulianDayNoon = Math.floor(iJulianDay - 0.5) + 0.5,
			iDaysSinceGregorianEpoch = iJulianDayNoon - GREGORIAN_EPOCH_DAYS,
			iQuadricent = Math.floor(iDaysSinceGregorianEpoch / 146097),
			iQuadricentNormalized = mod(iDaysSinceGregorianEpoch, 146097),
			iCent = Math.floor(iQuadricentNormalized / 36524),
			iCentNormalized = mod(iQuadricentNormalized, 36524),
			iQuad = Math.floor(iCentNormalized / 1461),
			iQuadNormalized = mod(iCentNormalized, 1461),
			iYearIndex = Math.floor(iQuadNormalized / 365),
			iYear = (iQuadricent * 400) + (iCent * 100) + (iQuad * 4) + iYearIndex,
			iMonth, iDay,
			iGregorianYearStartDays,
			iDayOfYear,
			tjd, tjd2,
			iLeapAdj, iLeapAdj2;

		if (!(iCent == 4 || iYearIndex == 4)) {
			iYear++;
		}

		iGregorianYearStartDays = GREGORIAN_EPOCH_DAYS + (365 * (iYear - 1)) + Math.floor((iYear - 1) / 4)
			- ( Math.floor((iYear - 1) / 100)) + Math.floor((iYear - 1) / 400);

		iDayOfYear = iJulianDayNoon - iGregorianYearStartDays;

		tjd = (GREGORIAN_EPOCH_DAYS - 1) + (365 * (iYear - 1)) + Math.floor((iYear - 1) / 4)
			- ( Math.floor((iYear - 1) / 100)) + Math.floor((iYear - 1) / 400) + Math.floor((739 / 12)
			+ ( (isGregorianLeapYear(iYear) ? -1 : -2)) + 1);

		iLeapAdj = 0;
		if (iJulianDayNoon < tjd) {
			iLeapAdj = 0;
		} else {
			iLeapAdj = isGregorianLeapYear(iYear) ? 1 : 2;
		}

		iMonth = Math.floor((((iDayOfYear + iLeapAdj) * 12) + 373) / 367);

		tjd2 = (GREGORIAN_EPOCH_DAYS - 1) + (365 * (iYear - 1))
			+ Math.floor((iYear - 1) / 4) - (Math.floor((iYear - 1) / 100))
			+ Math.floor((iYear - 1) / 400);

		iLeapAdj2 = 0;
		if (iMonth > 2) {
			iLeapAdj2 = isGregorianLeapYear(iYear) ? -1 : -2;
		}
		tjd2 += Math.floor((((367 * iMonth) - 362) / 12) + iLeapAdj2 + 1);

		iDay = (iJulianDayNoon - tjd2) + 1;

		return {
			day: iDay,
			month: iMonth - 1,
			year: iYear
		};
	}