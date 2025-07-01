private static String removeNumberFlag(String number) {
		// 去掉类型标识的结尾
		final int lastPos = number.length() - 1;
		final char lastCharUpper = Character.toUpperCase(number.charAt(lastPos));
		if ('D' == lastCharUpper || 'L' == lastCharUpper || 'F' == lastCharUpper) {
			number = StrUtil.subPre(number, lastPos);
		}
		return number;
	}