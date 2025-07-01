public BulkMutation add(@Nonnull ByteString rowKey, @Nonnull Mutation mutation) {
    Preconditions.checkNotNull(rowKey);
    Preconditions.checkNotNull(mutation);

    builder.addEntries(
        MutateRowsRequest.Entry.newBuilder()
            .setRowKey(rowKey)
            .addAllMutations(mutation.getMutations())
            .build());
    return this;
  }