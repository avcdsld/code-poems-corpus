private CompletableFuture<Boolean> abortTransaction(OperationContext context, String scope, String stream, long requestId) {
        return streamMetadataStore.getActiveTxns(scope, stream, context, executor)
                .thenCompose(activeTxns -> {
                    if (activeTxns == null || activeTxns.isEmpty()) {
                        return CompletableFuture.completedFuture(true);
                    } else {
                        // abort transactions
                        return Futures.allOf(activeTxns.entrySet().stream().map(txIdPair -> {
                            CompletableFuture<Void> voidCompletableFuture;
                            if (txIdPair.getValue().getTxnStatus().equals(TxnStatus.OPEN)) {
                                voidCompletableFuture = Futures.toVoid(streamTransactionMetadataTasks
                                        .abortTxn(scope, stream, txIdPair.getKey(), null, context)
                                        .exceptionally(e -> {
                                            Throwable cause = Exceptions.unwrap(e);
                                            if (cause instanceof StoreException.IllegalStateException ||
                                                    cause instanceof StoreException.WriteConflictException ||
                                                    cause instanceof StoreException.DataNotFoundException) {
                                                // IllegalStateException : The transaction is already in the process of being
                                                // completed. Ignore
                                                // WriteConflictException : Another thread is updating the transaction record.
                                                // ignore. We will effectively retry cleaning up the transaction if it is not
                                                // already being aborted.
                                                // DataNotFoundException: If transaction metadata is cleaned up after reading list
                                                // of active segments
                                                log.debug(requestId, "A known exception thrown during seal stream " +
                                                        "while trying to abort transaction on stream {}/{}", scope, stream, cause);
                                            } else {
                                                // throw the original exception
                                                // Note: we can ignore this error because if there are transactions found on a stream,
                                                // seal stream reposts the event back into request stream.
                                                // So in subsequent iteration it will reattempt to abort all active transactions.
                                                // This is a valid course of action because it is important to understand that
                                                // all transactions are completable (either via abort of commit).
                                                log.warn(requestId, "Exception thrown during seal stream while trying " +
                                                        "to abort transaction on stream {}/{}", scope, stream, cause);
                                            }
                                            return null;
                                        }));
                            } else {
                                voidCompletableFuture = CompletableFuture.completedFuture(null);
                            }

                            return voidCompletableFuture;
                        }).collect(Collectors.toList())).thenApply(v -> false);
                    }
                });
    }