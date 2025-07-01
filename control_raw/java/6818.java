public static String decode(String ciphertext, int offset) {
		final int len = ciphertext.length();
		final char[] plain = ciphertext.toCharArray();
		char c;
		for (int i = 0; i < len; i++) {
			c = ciphertext.charAt(i);
			if (false == Character.isLetter(c)) {
				continue;
			}
			plain[i] = decodeChar(c, offset);
		}
		return new String(plain);
	}