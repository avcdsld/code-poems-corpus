@BetaApi
  public final Operation deleteInterconnect(ProjectGlobalInterconnectName interconnect) {

    DeleteInterconnectHttpRequest request =
        DeleteInterconnectHttpRequest.newBuilder()
            .setInterconnect(interconnect == null ? null : interconnect.toString())
            .build();
    return deleteInterconnect(request);
  }