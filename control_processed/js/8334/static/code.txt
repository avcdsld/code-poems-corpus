function parseNumberAndCurrency(oConfig) {
		var sValue = oConfig.value;

		// Search for known symbols (longest match)
		// no distinction between default and custom currencies
		var oMatch = findLongestMatch(sValue, oConfig.currencySymbols);

		// Search for currency code
		if (!oMatch.code) {
			// before falling back to the default regex for ISO codes we check the
			// codes for custom currencies (if defined)
			oMatch = findLongestMatch(sValue, oConfig.customCurrencyCodes);

			if (!oMatch.code && !oConfig.customCurrenciesAvailable) {
				// Match 3-letter iso code
				var aIsoMatches = sValue.match(/(^[A-Z]{3}|[A-Z]{3}$)/);
				oMatch.code = aIsoMatches && aIsoMatches[0];
			}
		}

		// Remove symbol/code from value
		if (oMatch.code) {
			var iLastCodeIndex = oMatch.code.length - 1;
			var sLastCodeChar = oMatch.code.charAt(iLastCodeIndex);
			var iDelimiterPos;
			var rValidDelimiters = /[\-\s]+/;

			// Check whether last character of matched code is a number
			if (/\d$/.test(sLastCodeChar)) {
				// Check whether parse string starts with the matched code
				if (sValue.startsWith(oMatch.code)) {
					iDelimiterPos = iLastCodeIndex + 1;
					// \s matching any whitespace character including
					// non-breaking ws and invisible non-breaking ws
					if (!rValidDelimiters.test(sValue.charAt(iDelimiterPos))) {
						return undefined;
					}
				}
			// Check whether first character of matched code is a number
			} else if (/^\d/.test(oMatch.code)) {
				// Check whether parse string ends with the matched code
				if (sValue.endsWith(oMatch.code)) {
					iDelimiterPos = sValue.indexOf(oMatch.code) - 1;
					if (!rValidDelimiters.test(sValue.charAt(iDelimiterPos))) {
						return undefined;
					}
				}
			}
			sValue = sValue.replace(oMatch.symbol || oMatch.code, "");
		}

		// Set currency code to undefined, as the defined custom currencies
		// contain multiple currencies having the same symbol.
		if (oConfig.duplicatedSymbols && oConfig.duplicatedSymbols[oMatch.symbol]) {
			oMatch.code = undefined;
			Log.error("The parsed currency symbol '" + oMatch.symbol + "' is defined multiple " +
					"times in custom currencies.Therefore the result is not distinct.");
		}

		return {
			numberValue: sValue,
			currencyCode: oMatch.code || undefined
		};
	}