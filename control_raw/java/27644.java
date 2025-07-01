public CompletableFuture<ScaleStatusResponse> checkScale(String scope, String stream, int epoch,
                                                                        OperationContext context) {
        CompletableFuture<EpochRecord> activeEpochFuture =
                streamMetadataStore.getActiveEpoch(scope, stream, context, true, executor);
        CompletableFuture<State> stateFuture =
                streamMetadataStore.getState(scope, stream, true, context, executor);
        CompletableFuture<EpochTransitionRecord> etrFuture =
                streamMetadataStore.getEpochTransition(scope, stream, context, executor).thenApply(VersionedMetadata::getObject);
        return CompletableFuture.allOf(stateFuture, activeEpochFuture)
                        .handle((r, ex) -> {
                            ScaleStatusResponse.Builder response = ScaleStatusResponse.newBuilder();

                            if (ex != null) {
                                Throwable e = Exceptions.unwrap(ex);
                                if (e instanceof StoreException.DataNotFoundException) {
                                    response.setStatus(ScaleStatusResponse.ScaleStatus.INVALID_INPUT);
                                } else {
                                    response.setStatus(ScaleStatusResponse.ScaleStatus.INTERNAL_ERROR);
                                }
                            } else {
                                EpochRecord activeEpoch = activeEpochFuture.join();
                                State state = stateFuture.join();
                                EpochTransitionRecord etr = etrFuture.join();
                                if (epoch > activeEpoch.getEpoch()) {
                                    response.setStatus(ScaleStatusResponse.ScaleStatus.INVALID_INPUT);
                                } else if (activeEpoch.getEpoch() == epoch || activeEpoch.getReferenceEpoch() == epoch) {
                                    response.setStatus(ScaleStatusResponse.ScaleStatus.IN_PROGRESS);
                                } else {
                                    // active epoch == scale epoch + 1 but the state is scaling, the previous workflow 
                                    // has not completed.
                                    if (epoch + 1 == activeEpoch.getReferenceEpoch() && state.equals(State.SCALING) &&
                                            (etr.equals(EpochTransitionRecord.EMPTY) || etr.getNewEpoch() == activeEpoch.getEpoch())) {
                                        response.setStatus(ScaleStatusResponse.ScaleStatus.IN_PROGRESS);
                                    } else {
                                        response.setStatus(ScaleStatusResponse.ScaleStatus.SUCCESS);
                                    }
                                }
                            }
                                return response.build();
                            });
    }