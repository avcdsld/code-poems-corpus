public static void putFloatNormalizedKey(float value, MemorySegment target, int offset,
			int numBytes) {
		int iValue = Float.floatToIntBits(value);
		iValue ^= ((iValue >> (Integer.SIZE - 1)) | Integer.MIN_VALUE);
		NormalizedKeyUtil.putUnsignedIntegerNormalizedKey(iValue, target, offset, numBytes);
	}