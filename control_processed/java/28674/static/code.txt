@BetaApi
  public final Policy getIamPolicyNodeTemplate(ProjectRegionNodeTemplateResourceName resource) {

    GetIamPolicyNodeTemplateHttpRequest request =
        GetIamPolicyNodeTemplateHttpRequest.newBuilder()
            .setResource(resource == null ? null : resource.toString())
            .build();
    return getIamPolicyNodeTemplate(request);
  }