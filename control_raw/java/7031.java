public static void printProgress(char showChar, int len) {
		print("{}{}", CharUtil.CR, StrUtil.repeat(showChar, len));
	}