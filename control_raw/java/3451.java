public static final boolean endsWithDelimiter(byte[] bytes, int endPos, byte[] delim) {
		if (endPos < delim.length - 1) {
			return false;
		}
		for (int pos = 0; pos < delim.length; ++pos) {
			if (delim[pos] != bytes[endPos - delim.length + 1 + pos]) {
				return false;
			}
		}
		return true;
	}