@BetaApi
  public final Operation addRuleSecurityPolicy(
      String securityPolicy, SecurityPolicyRule securityPolicyRuleResource) {

    AddRuleSecurityPolicyHttpRequest request =
        AddRuleSecurityPolicyHttpRequest.newBuilder()
            .setSecurityPolicy(securityPolicy)
            .setSecurityPolicyRuleResource(securityPolicyRuleResource)
            .build();
    return addRuleSecurityPolicy(request);
  }