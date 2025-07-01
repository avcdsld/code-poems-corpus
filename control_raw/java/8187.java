public static String notContain(String textToSearch, String substring, String errorMsgTemplate, Object... params) throws IllegalArgumentException {
		if (StrUtil.isNotEmpty(textToSearch) && StrUtil.isNotEmpty(substring) && textToSearch.contains(substring)) {
			throw new IllegalArgumentException(StrUtil.format(errorMsgTemplate, params));
		}
		return substring;
	}