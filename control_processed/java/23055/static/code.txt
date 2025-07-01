public static Date parseDate(@NotNull String pattern, @NotNull String dateString) throws ParseException {
		return FastDateFormat.getInstance(pattern).parse(dateString);
	}