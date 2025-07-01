public static Date subSeconds(@NotNull final Date date, int amount) {
		return DateUtils.addSeconds(date, -amount);
	}