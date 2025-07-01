public static StreamSegmentReadResult read(SegmentHandle handle, long startOffset, int maxReadLength, int readBlockSize, ReadOnlyStorage storage) {
        Exceptions.checkArgument(startOffset >= 0, "startOffset", "startOffset must be a non-negative number.");
        Exceptions.checkArgument(maxReadLength >= 0, "maxReadLength", "maxReadLength must be a non-negative number.");
        Preconditions.checkNotNull(handle, "handle");
        Preconditions.checkNotNull(storage, "storage");
        String traceId = String.format("Read[%s]", handle.getSegmentName());

        // Build a SegmentInfo using the information we are given. If startOffset or length are incorrect, the underlying
        // ReadOnlyStorage will throw appropriate exceptions at the caller.
        StreamSegmentInformation segmentInfo = StreamSegmentInformation.builder().name(handle.getSegmentName())
                .startOffset(startOffset)
                .length(startOffset + maxReadLength)
                .build();
        return new StreamSegmentReadResult(startOffset, maxReadLength, new SegmentReader(segmentInfo, handle, readBlockSize, storage), traceId);
    }