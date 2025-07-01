public static int parseInt(String number) throws NumberFormatException {
		if (StrUtil.isBlank(number)) {
			return 0;
		}

		// 对于带小数转换为整数采取去掉小数的策略
		number = StrUtil.subBefore(number, CharUtil.DOT, false);
		if (StrUtil.isEmpty(number)) {
			return 0;
		}

		if (StrUtil.startWithIgnoreCase(number, "0x")) {
			// 0x04表示16进制数
			return Integer.parseInt(number.substring(2), 16);
		}

		return Integer.parseInt(removeNumberFlag(number));
	}