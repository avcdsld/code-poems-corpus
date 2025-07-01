@BetaApi
  public final Operation stopInstance(ProjectZoneInstanceName instance) {

    StopInstanceHttpRequest request =
        StopInstanceHttpRequest.newBuilder()
            .setInstance(instance == null ? null : instance.toString())
            .build();
    return stopInstance(request);
  }