private static String toChinese(int amountPart, boolean isUseTraditional) {
//		if (amountPart < 0 || amountPart > 10000) {
//			throw new IllegalArgumentException("Number must 0 < num < 10000！");
//		}

		String[] numArray = isUseTraditional ? traditionalDigits : simpleDigits;
		String[] units = isUseTraditional ? traditionalUnits : simpleUnits;

		int temp = amountPart;

		String chineseStr = "";
		boolean lastIsZero = true; // 在从低位往高位循环时，记录上一位数字是不是 0
		for (int i = 0; temp > 0; i++) {
			if (temp == 0) {
				// 高位已无数据
				break;
			}
			int digit = temp % 10;
			if (digit == 0) { // 取到的数字为 0
				if (false == lastIsZero) {
					// 前一个数字不是 0，则在当前汉字串前加“零”字;
					chineseStr = "零" + chineseStr;
				}
				lastIsZero = true;
			} else { // 取到的数字不是 0
				chineseStr = numArray[digit] + units[i] + chineseStr;
				lastIsZero = false;
			}
			temp = temp / 10;
		}
		return chineseStr;
	}