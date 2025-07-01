public static boolean bitGet(MemorySegment segment, int baseOffset, int index) {
		int offset = baseOffset + ((index & BIT_BYTE_POSITION_MASK) >>> 3);
		byte current = segment.get(offset);
		return (current & (1 << (index & BIT_BYTE_INDEX_MASK))) != 0;
	}