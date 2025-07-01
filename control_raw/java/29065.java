@BetaApi
  public final Operation setSecurityPolicyBackendService(
      String backendService, SecurityPolicyReference securityPolicyReferenceResource) {

    SetSecurityPolicyBackendServiceHttpRequest request =
        SetSecurityPolicyBackendServiceHttpRequest.newBuilder()
            .setBackendService(backendService)
            .setSecurityPolicyReferenceResource(securityPolicyReferenceResource)
            .build();
    return setSecurityPolicyBackendService(request);
  }