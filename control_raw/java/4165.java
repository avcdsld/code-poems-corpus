static byte[] readBinaryFieldFromSegments(
			MemorySegment[] segments, int baseOffset, int fieldOffset,
			long variablePartOffsetAndLen) {
		long mark = variablePartOffsetAndLen & HIGHEST_FIRST_BIT;
		if (mark == 0) {
			final int subOffset = (int) (variablePartOffsetAndLen >> 32);
			final int len = (int) variablePartOffsetAndLen;
			return SegmentsUtil.copyToBytes(segments, baseOffset + subOffset, len);
		} else {
			int len = (int) ((variablePartOffsetAndLen & HIGHEST_SECOND_TO_EIGHTH_BIT) >>> 56);
			if (SegmentsUtil.LITTLE_ENDIAN) {
				return SegmentsUtil.copyToBytes(segments, fieldOffset, len);
			} else {
				// fieldOffset + 1 to skip header.
				return SegmentsUtil.copyToBytes(segments, fieldOffset + 1, len);
			}
		}
	}