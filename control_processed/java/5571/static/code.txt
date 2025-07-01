public static int hashUnsafeBytes(Object base, long offset, int lengthInBytes) {
		return hashUnsafeBytes(base, offset, lengthInBytes, DEFAULT_SEED);
	}