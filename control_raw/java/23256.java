public static Date beginOfHour(@NotNull final Date date) {
		return DateUtils.truncate(date, Calendar.HOUR_OF_DAY);
	}