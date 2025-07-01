public static StreamCutInternal from(String base64String) {
        Exceptions.checkNotNullOrEmpty(base64String, "base64String");
        String[] split = decompressFromBase64(base64String).split(":", 5);
        Preconditions.checkArgument(split.length == 5, "Invalid string representation of StreamCut");

        final Stream stream = Stream.of(split[1]);
        List<Integer> segmentNumbers = stringToList(split[2], Integer::valueOf);
        List<Integer> epochs = stringToList(split[3], Integer::valueOf);
        List<Long> offsets = stringToList(split[4], Long::valueOf);

        final Map<Segment, Long> positions = IntStream.range(0, segmentNumbers.size()).boxed()
                .collect(Collectors.toMap(i ->  new Segment(stream.getScope(), stream.getStreamName(),
                                                            StreamSegmentNameUtils.computeSegmentId(segmentNumbers.get(i), epochs.get(i))),
                                          offsets::get));
        return new StreamCutImpl(stream, positions);
    }