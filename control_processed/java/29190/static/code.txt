@BetaApi
  public final Operation setProxyHeaderTargetSslProxy(
      ProjectGlobalTargetSslProxyName targetSslProxy,
      TargetSslProxiesSetProxyHeaderRequest targetSslProxiesSetProxyHeaderRequestResource) {

    SetProxyHeaderTargetSslProxyHttpRequest request =
        SetProxyHeaderTargetSslProxyHttpRequest.newBuilder()
            .setTargetSslProxy(targetSslProxy == null ? null : targetSslProxy.toString())
            .setTargetSslProxiesSetProxyHeaderRequestResource(
                targetSslProxiesSetProxyHeaderRequestResource)
            .build();
    return setProxyHeaderTargetSslProxy(request);
  }