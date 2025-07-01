public Long toLong() {
		ensureMaterialized();
		if (sizeInBytes == 0) {
			return null;
		}
		int size = segments[0].size();
		SegmentAndOffset segmentAndOffset = startSegmentAndOffset(size);
		int totalOffset = 0;

		byte b = segmentAndOffset.value();
		final boolean negative = b == '-';
		if (negative || b == '+') {
			segmentAndOffset.nextByte(size);
			totalOffset++;
			if (sizeInBytes == 1) {
				return null;
			}
		}

		long result = 0;
		final byte separator = '.';
		final int radix = 10;
		final long stopValue = Long.MIN_VALUE / radix;
		while (totalOffset < this.sizeInBytes) {
			b = segmentAndOffset.value();
			totalOffset++;
			segmentAndOffset.nextByte(size);
			if (b == separator) {
				// We allow decimals and will return a truncated integral in that case.
				// Therefore we won't throw an exception here (checking the fractional
				// part happens below.)
				break;
			}

			int digit;
			if (b >= '0' && b <= '9') {
				digit = b - '0';
			} else {
				return null;
			}

			// We are going to process the new digit and accumulate the result. However, before
			// doing this, if the result is already smaller than the
			// stopValue(Long.MIN_VALUE / radix), then result * 10 will definitely be smaller
			// than minValue, and we can stop.
			if (result < stopValue) {
				return null;
			}

			result = result * radix - digit;
			// Since the previous result is less than or equal to
			// stopValue(Long.MIN_VALUE / radix), we can just use `result > 0` to check overflow.
			// If result overflows, we should stop.
			if (result > 0) {
				return null;
			}
		}

		// This is the case when we've encountered a decimal separator. The fractional
		// part will not change the number, but we will verify that the fractional part
		// is well formed.
		while (totalOffset < sizeInBytes) {
			byte currentByte = segmentAndOffset.value();
			if (currentByte < '0' || currentByte > '9') {
				return null;
			}
			totalOffset++;
			segmentAndOffset.nextByte(size);
		}

		if (!negative) {
			result = -result;
			if (result < 0) {
				return null;
			}
		}
		return result;
	}