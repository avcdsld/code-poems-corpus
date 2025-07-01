@BetaApi
  public final Operation deleteForwardingRule(String forwardingRule) {

    DeleteForwardingRuleHttpRequest request =
        DeleteForwardingRuleHttpRequest.newBuilder().setForwardingRule(forwardingRule).build();
    return deleteForwardingRule(request);
  }