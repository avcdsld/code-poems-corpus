@BetaApi
  public final Operation attachNetworkEndpointsNetworkEndpointGroup(
      ProjectZoneNetworkEndpointGroupName networkEndpointGroup,
      NetworkEndpointGroupsAttachEndpointsRequest
          networkEndpointGroupsAttachEndpointsRequestResource) {

    AttachNetworkEndpointsNetworkEndpointGroupHttpRequest request =
        AttachNetworkEndpointsNetworkEndpointGroupHttpRequest.newBuilder()
            .setNetworkEndpointGroup(
                networkEndpointGroup == null ? null : networkEndpointGroup.toString())
            .setNetworkEndpointGroupsAttachEndpointsRequestResource(
                networkEndpointGroupsAttachEndpointsRequestResource)
            .build();
    return attachNetworkEndpointsNetworkEndpointGroup(request);
  }