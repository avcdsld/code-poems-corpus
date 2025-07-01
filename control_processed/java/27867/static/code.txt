private FlushArgs getFlushArgs() throws DataCorruptionException {
        StorageOperation first = this.operations.getFirst();
        if (!(first instanceof AggregatedAppendOperation)) {
            // Nothing to flush - first operation is not an AggregatedAppend.
            return new FlushArgs(null, 0, Collections.emptyMap());
        }

        AggregatedAppendOperation appendOp = (AggregatedAppendOperation) first;
        int length = (int) appendOp.getLength();
        InputStream data;
        if (length > 0) {
            data = this.dataSource.getAppendData(appendOp.getStreamSegmentId(), appendOp.getStreamSegmentOffset(), length);
            if (data == null) {
                if (this.metadata.isDeleted()) {
                    // Segment was deleted - nothing more to do.
                    return new FlushArgs(null, 0, Collections.emptyMap());
                }
                throw new DataCorruptionException(String.format("Unable to retrieve CacheContents for '%s'.", appendOp));
            }
        } else {
            if (appendOp.attributes.isEmpty()) {
                throw new DataCorruptionException(String.format("Found AggregatedAppendOperation with no data or attributes: '%s'.", appendOp));
            }
            data = null;
        }

        appendOp.seal();
        return new FlushArgs(data, length, appendOp.attributes);
    }