public static Decimal fromUnscaledBytes(int precision, int scale, byte[] bytes) {
		if (precision > MAX_COMPACT_PRECISION) {
			BigDecimal bd = new BigDecimal(new BigInteger(bytes), scale);
			return new Decimal(precision, scale, -1, bd);
		}
		assert bytes.length == 8;
		long l = 0;
		for (int i = 0; i < 8; i++) {
			l <<= 8;
			l |= (bytes[i] & (0xff));
		}
		return new Decimal(precision, scale, l, null);
	}