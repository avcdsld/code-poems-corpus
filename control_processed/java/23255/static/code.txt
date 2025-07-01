public static Date nextDate(@NotNull final Date date) {
		return DateUtils.ceiling(date, Calendar.DATE);
	}