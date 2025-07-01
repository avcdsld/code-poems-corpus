@Override
    public ReadResultEntry next() {
        Exceptions.checkNotClosed(this.closed, this);

        // If the previous entry hasn't finished yet, we cannot proceed.
        Preconditions.checkState(this.lastEntryFuture == null || this.lastEntryFuture.isDone(), "Cannot request a new entry when the previous one hasn't completed retrieval yet.");
        if (this.lastEntryFuture != null && !this.lastEntryFuture.isDone()) {
            this.lastEntryFuture.join();
        }

        // Only check for hasNext now, after we have waited for the previous entry to finish - since that updates
        // some fields that hasNext relies on.
        if (!hasNext()) {
            return null;
        }

        // Retrieve the next item.
        long startOffset = this.streamSegmentStartOffset + this.consumedLength;
        int remainingLength = this.maxResultLength - this.consumedLength;
        CompletableReadResultEntry entry = this.getNextItem.apply(startOffset, remainingLength);

        if (entry == null) {
            assert remainingLength <= 0 : String.format("No ReadResultEntry received when one was expected. Offset %d, MaxLen %d.", startOffset, remainingLength);
            this.lastEntryFuture = null;
        } else {
            assert entry.getStreamSegmentOffset() == startOffset : String.format("Invalid ReadResultEntry. Expected offset %d, given %d.", startOffset, entry.getStreamSegmentOffset());
            if (entry.getType().isTerminal()) {
                // We encountered Terminal Entry, which means we cannot read anymore using this ReadResult.
                // This can be the case if either the StreamSegment has been truncated beyond the current ReadResult offset,
                // or if the StreamSegment is now sealed and we have requested an offset that is beyond the StreamSegment
                // length. We cannot continue reading; close the ReadResult and return the appropriate Result Entry.
                // If we don't close the ReadResult, hasNext() will erroneously return true and next() will have undefined behavior.
                this.lastEntryFuture = null;
                this.canRead = false;
            } else {
                // After the previous entry is done, update the consumedLength value.
                entry.setCompletionCallback(length -> this.consumedLength += length);
                this.lastEntryFuture = entry.getContent();

                // Check, again, if we are closed. It is possible that this Result was closed after the last check
                // and before we got the lastEntryFuture. If this happened, throw the exception and don't return anything.
                Exceptions.checkNotClosed(this.closed, this);
            }
        }

        log.trace("{}.ReadResult[{}]: Consumed = {}, MaxLength = {}, Entry = ({}).", this.traceObjectId, this.streamSegmentStartOffset, this.consumedLength, this.maxResultLength, entry);
        return entry;
    }