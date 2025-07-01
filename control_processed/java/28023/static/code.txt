public static final Segment encode(final SegmentId segment) {
        Preconditions.checkNotNull(segment, "segment");
        return new Segment(segment.getStreamInfo().getScope(),
                segment.getStreamInfo().getStream(),
                segment.getSegmentId());
    }