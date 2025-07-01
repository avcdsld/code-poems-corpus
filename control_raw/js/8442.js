function getSingleFilterValue(oFilter, sEdmType, bWithinAnd) {
			var sFilter,
				sValue = _Helper.formatLiteral(oFilter.oValue1, sEdmType),
				sFilterPath = decodeURIComponent(oFilter.sPath);

			switch (oFilter.sOperator) {
				case FilterOperator.BT :
					sFilter = sFilterPath + " ge " + sValue + " and " + sFilterPath + " le "
						+ _Helper.formatLiteral(oFilter.oValue2, sEdmType);
					break;
				case FilterOperator.NB :
					sFilter = wrap(sFilterPath + " lt " + sValue + " or " + sFilterPath + " gt "
						+ _Helper.formatLiteral(oFilter.oValue2, sEdmType), bWithinAnd);
					break;
				case FilterOperator.EQ :
				case FilterOperator.GE :
				case FilterOperator.GT :
				case FilterOperator.LE :
				case FilterOperator.LT :
				case FilterOperator.NE :
					sFilter = sFilterPath + " " + oFilter.sOperator.toLowerCase() + " " + sValue;
					break;
				case FilterOperator.Contains :
				case FilterOperator.EndsWith :
				case FilterOperator.NotContains :
				case FilterOperator.NotEndsWith :
				case FilterOperator.NotStartsWith :
				case FilterOperator.StartsWith :
					sFilter = oFilter.sOperator.toLowerCase().replace("not", "not ")
						+ "(" + sFilterPath + "," + sValue + ")";
					break;
				default :
					throw new Error("Unsupported operator: " + oFilter.sOperator);
			}
			return sFilter;
		}