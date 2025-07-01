@BetaApi
  public final BackendService getRegionBackendService(
      ProjectRegionBackendServiceName backendService) {

    GetRegionBackendServiceHttpRequest request =
        GetRegionBackendServiceHttpRequest.newBuilder()
            .setBackendService(backendService == null ? null : backendService.toString())
            .build();
    return getRegionBackendService(request);
  }