boolean hasReadableBytes(int count) {
        if (count < 0 || count > MAX_COUNT_OF_READABLE_BYTES) {
            throw new IllegalArgumentException("count: " + count
                    + " (expected: 0-" + MAX_COUNT_OF_READABLE_BYTES + ')');
        }
        return hasReadableBits(count << 3);
    }