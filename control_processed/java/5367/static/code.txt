public KeyGroupRangeOffsets getIntersection(KeyGroupRange keyGroupRange) {
		Preconditions.checkNotNull(keyGroupRange);
		KeyGroupRange intersection = this.keyGroupRange.getIntersection(keyGroupRange);
		long[] subOffsets = new long[intersection.getNumberOfKeyGroups()];
		if(subOffsets.length > 0) {
			System.arraycopy(
					offsets,
					computeKeyGroupIndex(intersection.getStartKeyGroup()),
					subOffsets,
					0,
					subOffsets.length);
		}
		return new KeyGroupRangeOffsets(intersection, subOffsets);
	}