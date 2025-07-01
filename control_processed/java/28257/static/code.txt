@BetaApi
  public final Operation removePeeringNetwork(
      String network, NetworksRemovePeeringRequest networksRemovePeeringRequestResource) {

    RemovePeeringNetworkHttpRequest request =
        RemovePeeringNetworkHttpRequest.newBuilder()
            .setNetwork(network)
            .setNetworksRemovePeeringRequestResource(networksRemovePeeringRequestResource)
            .build();
    return removePeeringNetwork(request);
  }