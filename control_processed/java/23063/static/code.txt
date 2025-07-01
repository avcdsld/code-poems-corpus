public static boolean isIdCard(@Nullable CharSequence input) {
		return isMatch(PATTERN_REGEX_ID_CARD15, input) || isMatch(PATTERN_REGEX_ID_CARD18, input);
	}