@BetaApi
  public final Operation setSchedulingInstance(
      ProjectZoneInstanceName instance, Scheduling schedulingResource) {

    SetSchedulingInstanceHttpRequest request =
        SetSchedulingInstanceHttpRequest.newBuilder()
            .setInstance(instance == null ? null : instance.toString())
            .setSchedulingResource(schedulingResource)
            .build();
    return setSchedulingInstance(request);
  }