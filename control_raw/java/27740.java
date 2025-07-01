void preProcessOperation(StreamSegmentAppendOperation operation) throws StreamSegmentSealedException, StreamSegmentMergedException,
            BadOffsetException, BadAttributeUpdateException {
        ensureSegmentId(operation);
        if (this.merged) {
            // We do not allow any operation after merging (since after merging the Segment disappears).
            throw new StreamSegmentMergedException(this.name);
        }

        if (this.sealed) {
            throw new StreamSegmentSealedException(this.name);
        }

        if (!this.recoveryMode) {
            // Offset check (if append-with-offset).
            long operationOffset = operation.getStreamSegmentOffset();
            if (operationOffset >= 0) {
                // If the Operation already has an offset assigned, verify that it matches the current end offset of the Segment.
                if (operationOffset != this.length) {
                    throw new BadOffsetException(this.name, this.length, operationOffset);
                }
            } else {
                // No pre-assigned offset. Put the Append at the end of the Segment.
                operation.setStreamSegmentOffset(this.length);
            }

            // Attribute validation.
            preProcessAttributes(operation.getAttributeUpdates());
        }
    }