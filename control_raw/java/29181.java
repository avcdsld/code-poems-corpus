@BetaApi
  public final Operation deleteTargetSslProxy(String targetSslProxy) {

    DeleteTargetSslProxyHttpRequest request =
        DeleteTargetSslProxyHttpRequest.newBuilder().setTargetSslProxy(targetSslProxy).build();
    return deleteTargetSslProxy(request);
  }