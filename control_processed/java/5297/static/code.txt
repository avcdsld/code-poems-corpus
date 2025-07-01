public static void copyFromBytes(
			MemorySegment[] segments, int offset,
			byte[] bytes, int bytesOffset, int numBytes) {
		if (segments.length == 1) {
			segments[0].put(offset, bytes, bytesOffset, numBytes);
		} else {
			copyMultiSegmentsFromBytes(segments, offset, bytes, bytesOffset, numBytes);
		}
	}