@BetaApi
  public final Operation setUrlMapTargetHttpsProxy(
      String targetHttpsProxy, UrlMapReference urlMapReferenceResource) {

    SetUrlMapTargetHttpsProxyHttpRequest request =
        SetUrlMapTargetHttpsProxyHttpRequest.newBuilder()
            .setTargetHttpsProxy(targetHttpsProxy)
            .setUrlMapReferenceResource(urlMapReferenceResource)
            .build();
    return setUrlMapTargetHttpsProxy(request);
  }