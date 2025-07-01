@Override
    public boolean shouldRequestContents(ReadResultEntryType entryType, long streamSegmentOffset) {
        // We only care about data that has already been written, so this implies Cache and Storage.
        // Additionally, given that the Store acks an append prior to inserting it into the cache (but after the metadata
        // update), we may occasionally get Future reads. We should accept those too, as they should be completed shortly.
        return entryType == ReadResultEntryType.Cache || entryType == ReadResultEntryType.Storage || entryType == ReadResultEntryType.Future;
    }