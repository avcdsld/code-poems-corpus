@BetaApi
  public final Autoscaler getRegionAutoscaler(String autoscaler) {

    GetRegionAutoscalerHttpRequest request =
        GetRegionAutoscalerHttpRequest.newBuilder().setAutoscaler(autoscaler).build();
    return getRegionAutoscaler(request);
  }