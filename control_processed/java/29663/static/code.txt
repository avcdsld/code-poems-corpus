@BetaApi
  public final ListInstancesInstanceGroupsPagedResponse listInstancesInstanceGroups(
      String instanceGroup,
      InstanceGroupsListInstancesRequest instanceGroupsListInstancesRequestResource) {
    ListInstancesInstanceGroupsHttpRequest request =
        ListInstancesInstanceGroupsHttpRequest.newBuilder()
            .setInstanceGroup(instanceGroup)
            .setInstanceGroupsListInstancesRequestResource(
                instanceGroupsListInstancesRequestResource)
            .build();
    return listInstancesInstanceGroups(request);
  }