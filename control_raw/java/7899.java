public static <T> int count(Iterable<T> iterable, Matcher<T> matcher) {
		int count = 0;
		if (null != iterable) {
			for (T t : iterable) {
				if (null == matcher || matcher.match(t)) {
					count++;
				}
			}
		}
		return count;
	}