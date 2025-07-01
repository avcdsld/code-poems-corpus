@BetaApi
  public final SslPolicy getSslPolicy(ProjectGlobalSslPolicyName sslPolicy) {

    GetSslPolicyHttpRequest request =
        GetSslPolicyHttpRequest.newBuilder()
            .setSslPolicy(sslPolicy == null ? null : sslPolicy.toString())
            .build();
    return getSslPolicy(request);
  }