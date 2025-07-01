@BetaApi(
      "The surface for long-running operations is not stable yet and may change in the future.")
  public final OperationFuture<AppProfile, UpdateAppProfileMetadata> updateAppProfileAsync(
      AppProfile appProfile, FieldMask updateMask) {

    UpdateAppProfileRequest request =
        UpdateAppProfileRequest.newBuilder()
            .setAppProfile(appProfile)
            .setUpdateMask(updateMask)
            .build();
    return updateAppProfileAsync(request);
  }