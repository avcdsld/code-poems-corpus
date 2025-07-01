public static void bitUnSet(MemorySegment segment, int baseOffset, int index) {
		int offset = baseOffset + ((index & BIT_BYTE_POSITION_MASK) >>> 3);
		byte current = segment.get(offset);
		current &= ~(1 << (index & BIT_BYTE_INDEX_MASK));
		segment.put(offset, current);
	}