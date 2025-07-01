private void updateIndex(
			long key,
			int hashCode,
			long address,
			int size,
			MemorySegment dataSegment,
			int currentPositionInSegment) throws IOException {
		assert (numKeys <= numBuckets / 2);
		int bucketId = hashCode & numBucketsMask;

		// each bucket occupied 16 bytes (long key + long pointer to data address)
		int bucketOffset = bucketId * SPARSE_BUCKET_ELEMENT_SIZE_IN_BYTES;
		MemorySegment segment = buckets[bucketOffset >>> segmentSizeBits];
		int segOffset = bucketOffset & segmentSizeMask;
		long currAddress;

		while (true) {
			currAddress = segment.getLong(segOffset + 8);
			if (segment.getLong(segOffset) != key && currAddress != INVALID_ADDRESS) {
				// hash conflicts, the bucket is occupied by another key

				// TODO test Conflict resolution:
				// now:    +1 +1 +1... cache friendly but more conflict, so we set factor to 0.5
				// other1: +1 +2 +3... less conflict, factor can be 0.75
				// other2: Secondary hashCode... less and less conflict, but need compute hash again
				bucketId = (bucketId + 1) & numBucketsMask;
				if (segOffset + SPARSE_BUCKET_ELEMENT_SIZE_IN_BYTES < segmentSize) {
					// if the new bucket still in current segment, we only need to update offset
					// within this segment
					segOffset += SPARSE_BUCKET_ELEMENT_SIZE_IN_BYTES;
				} else {
					// otherwise, we should re-calculate segment and offset
					bucketOffset = bucketId * 16;
					segment = buckets[bucketOffset >>> segmentSizeBits];
					segOffset = bucketOffset & segmentSizeMask;
				}
			} else {
				break;
			}
		}
		if (currAddress == INVALID_ADDRESS) {
			// this is the first value for this key, put the address in array.
			segment.putLong(segOffset, key);
			segment.putLong(segOffset + 8, address);
			numKeys += 1;
			// dataSegment may be null if we only have to rehash bucket area
			if (dataSegment != null) {
				dataSegment.putLong(currentPositionInSegment, toAddrAndLen(INVALID_ADDRESS, size));
			}
			if (numKeys * 2 > numBuckets) {
				resize();
			}
		} else {
			// there are some values for this key, put the address in the front of them.
			dataSegment.putLong(currentPositionInSegment, toAddrAndLen(currAddress, size));
			segment.putLong(segOffset + 8, address);
		}
	}