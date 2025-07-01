@BetaApi(
      "The surface for long-running operations is not stable yet and may change in the future.")
  public final OperationFuture<Instance, UpdateInstanceMetadata> partialUpdateInstanceAsync(
      PartialUpdateInstanceRequest request) {
    return partialUpdateInstanceOperationCallable().futureCall(request);
  }