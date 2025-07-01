public static Decimal sign(Decimal b0) {
		if (b0.isCompact()) {
			return new Decimal(b0.precision, b0.scale, b0.signum() * POW10[b0.scale], null);
		} else {
			return fromBigDecimal(BigDecimal.valueOf(b0.signum()), b0.precision, b0.scale);
		}
	}