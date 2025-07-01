@Override
    public long getLowestUncommittedSequenceNumber() {
        StorageOperation first = this.operations.getFirst();
        return first == null ? Operation.NO_SEQUENCE_NUMBER : first.getSequenceNumber();
    }