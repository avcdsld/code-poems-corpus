@BetaApi
  public final Operation setServiceAccountInstance(
      ProjectZoneInstanceName instance,
      InstancesSetServiceAccountRequest instancesSetServiceAccountRequestResource) {

    SetServiceAccountInstanceHttpRequest request =
        SetServiceAccountInstanceHttpRequest.newBuilder()
            .setInstance(instance == null ? null : instance.toString())
            .setInstancesSetServiceAccountRequestResource(instancesSetServiceAccountRequestResource)
            .build();
    return setServiceAccountInstance(request);
  }