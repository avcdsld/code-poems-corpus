public static BigDecimal div(Number v1, Number v2, int scale, RoundingMode roundingMode) {
		return div(v1.toString(), v2.toString(), scale, roundingMode);
	}