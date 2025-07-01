@BetaApi
  public final Operation setBackupTargetPool(
      String targetPool, Float failoverRatio, TargetReference targetReferenceResource) {

    SetBackupTargetPoolHttpRequest request =
        SetBackupTargetPoolHttpRequest.newBuilder()
            .setTargetPool(targetPool)
            .setFailoverRatio(failoverRatio)
            .setTargetReferenceResource(targetReferenceResource)
            .build();
    return setBackupTargetPool(request);
  }