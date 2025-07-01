@BetaApi
  public final Operation detachNetworkEndpointsNetworkEndpointGroup(
      ProjectZoneNetworkEndpointGroupName networkEndpointGroup,
      NetworkEndpointGroupsDetachEndpointsRequest
          networkEndpointGroupsDetachEndpointsRequestResource) {

    DetachNetworkEndpointsNetworkEndpointGroupHttpRequest request =
        DetachNetworkEndpointsNetworkEndpointGroupHttpRequest.newBuilder()
            .setNetworkEndpointGroup(
                networkEndpointGroup == null ? null : networkEndpointGroup.toString())
            .setNetworkEndpointGroupsDetachEndpointsRequestResource(
                networkEndpointGroupsDetachEndpointsRequestResource)
            .build();
    return detachNetworkEndpointsNetworkEndpointGroup(request);
  }