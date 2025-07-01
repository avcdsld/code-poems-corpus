@BetaApi
  public final Operation detachNetworkEndpointsNetworkEndpointGroup(
      String networkEndpointGroup,
      NetworkEndpointGroupsDetachEndpointsRequest
          networkEndpointGroupsDetachEndpointsRequestResource) {

    DetachNetworkEndpointsNetworkEndpointGroupHttpRequest request =
        DetachNetworkEndpointsNetworkEndpointGroupHttpRequest.newBuilder()
            .setNetworkEndpointGroup(networkEndpointGroup)
            .setNetworkEndpointGroupsDetachEndpointsRequestResource(
                networkEndpointGroupsDetachEndpointsRequestResource)
            .build();
    return detachNetworkEndpointsNetworkEndpointGroup(request);
  }