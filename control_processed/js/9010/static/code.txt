function() {
			// Lookup into global Config
			var mCustomCurrencies = this._get("currency"),
				mCustomCurrencySymbols = {},
				sIsoCode;

			for (var sCurrencyKey in mCustomCurrencies) {
				sIsoCode = mCustomCurrencies[sCurrencyKey].isoCode;

				if (mCustomCurrencies[sCurrencyKey].symbol) {
					mCustomCurrencySymbols[sCurrencyKey] = mCustomCurrencies[sCurrencyKey].symbol;
				} else if (sIsoCode) {
					mCustomCurrencySymbols[sCurrencyKey] = this._get("currencySymbols")[sIsoCode];
				}
			}

			return Object.assign({}, this._get("currencySymbols"), mCustomCurrencySymbols);
		}