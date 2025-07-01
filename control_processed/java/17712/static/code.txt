public long writeFinishStaticMarker() throws IOException {
        Preconditions.checkState(endStaticInfoOffset < 0, "Wrote final static already information already");
        Pair<Integer, FlatBufferBuilder> encoded = encodeStaticHeader(UIInfoType.START_EVENTS);
        long out = append(encoded.getSecond(), null);
        endStaticInfoOffset = file.length();
        return out;
    }