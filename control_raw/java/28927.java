@BetaApi(
      "The surface for long-running operations is not stable yet and may change in the future.")
  public final OperationFuture<Empty, KnowledgeOperationMetadata> deleteDocumentAsync(
      DeleteDocumentRequest request) {
    return deleteDocumentOperationCallable().futureCall(request);
  }