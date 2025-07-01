public static byte[] encodeUTF8(String str) {
		byte[] bytes = allocateReuseBytes(str.length() * MAX_BYTES_PER_CHAR);
		int len = encodeUTF8(str, bytes);
		return Arrays.copyOf(bytes, len);
	}