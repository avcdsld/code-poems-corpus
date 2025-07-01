public static Long toTimestampTz(String dateStr, String format, String tzStr) {
		TimeZone tz = TIMEZONE_CACHE.get(tzStr);
		return toTimestamp(dateStr, format, tz);
	}