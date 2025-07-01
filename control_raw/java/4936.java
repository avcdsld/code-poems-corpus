public static Calendar parseDateFormat(String s, DateFormat dateFormat,
										   TimeZone tz) {
		ParsePosition pp = new ParsePosition(0);
		Calendar ret = parseDateFormat(s, dateFormat, tz, pp);
		if (pp.getIndex() != s.length()) {
			// Didn't consume entire string - not good
			return null;
		}
		return ret;
	}