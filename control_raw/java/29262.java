@BetaApi
  public final Operation insertSecurityPolicy(
      String project, SecurityPolicy securityPolicyResource) {

    InsertSecurityPolicyHttpRequest request =
        InsertSecurityPolicyHttpRequest.newBuilder()
            .setProject(project)
            .setSecurityPolicyResource(securityPolicyResource)
            .build();
    return insertSecurityPolicy(request);
  }