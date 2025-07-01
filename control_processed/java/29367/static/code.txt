@BetaApi
  public final AggregatedListNetworkEndpointGroupsPagedResponse aggregatedListNetworkEndpointGroups(
      String project) {
    AggregatedListNetworkEndpointGroupsHttpRequest request =
        AggregatedListNetworkEndpointGroupsHttpRequest.newBuilder().setProject(project).build();
    return aggregatedListNetworkEndpointGroups(request);
  }