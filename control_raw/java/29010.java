@BetaApi(
      "The surface for long-running operations is not stable yet and may change in the future.")
  public final OperationFuture<AsyncBatchAnnotateImagesResponse, OperationMetadata>
      asyncBatchAnnotateImagesAsync(AsyncBatchAnnotateImagesRequest request) {
    return asyncBatchAnnotateImagesOperationCallable().futureCall(request);
  }