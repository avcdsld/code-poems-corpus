private CompletableFuture<Void> validateConditionalUpdate(DirectSegmentAccess segment, TableKeyBatch batch, TimeoutTimer timer) {
        Exceptions.checkNotClosed(this.closed.get(), this);
        List<UUID> hashes = batch.getVersionedItems().stream()
                .map(TableKeyBatch.Item::getHash)
                .collect(Collectors.toList());
        CompletableFuture<Void> result = getBucketOffsets(segment, hashes, timer)
                .thenAccept(offsets -> validateConditionalUpdate(batch.getVersionedItems(), offsets, segment.getInfo().getName()));
        return Futures.exceptionallyCompose(
                result,
                ex -> {
                    ex = Exceptions.unwrap(ex);
                    if (ex instanceof BadKeyVersionException) {
                        return validateConditionalUpdateFailures(segment, ((BadKeyVersionException) ex).getExpectedVersions(), timer);
                    }

                    // Some other exception. Re-throw.
                    return Futures.failedFuture(ex);
                });
    }