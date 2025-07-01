public static boolean containsInvalid(String fileName) {
		return StrUtil.isBlank(fileName) ? false : ReUtil.contains(FILE_NAME_INVALID_PATTERN_WIN, fileName);
	}