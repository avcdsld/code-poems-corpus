@BetaApi
  public final Operation startInstance(ProjectZoneInstanceName instance) {

    StartInstanceHttpRequest request =
        StartInstanceHttpRequest.newBuilder()
            .setInstance(instance == null ? null : instance.toString())
            .build();
    return startInstance(request);
  }