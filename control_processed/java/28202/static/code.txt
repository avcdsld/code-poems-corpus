@BetaApi
  public final ListSslPoliciesPagedResponse listSslPolicies(ProjectName project) {
    ListSslPoliciesHttpRequest request =
        ListSslPoliciesHttpRequest.newBuilder()
            .setProject(project == null ? null : project.toString())
            .build();
    return listSslPolicies(request);
  }