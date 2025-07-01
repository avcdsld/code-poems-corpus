@BetaApi
  public final Operation startWithEncryptionKeyInstance(
      ProjectZoneInstanceName instance,
      InstancesStartWithEncryptionKeyRequest instancesStartWithEncryptionKeyRequestResource) {

    StartWithEncryptionKeyInstanceHttpRequest request =
        StartWithEncryptionKeyInstanceHttpRequest.newBuilder()
            .setInstance(instance == null ? null : instance.toString())
            .setInstancesStartWithEncryptionKeyRequestResource(
                instancesStartWithEncryptionKeyRequestResource)
            .build();
    return startWithEncryptionKeyInstance(request);
  }