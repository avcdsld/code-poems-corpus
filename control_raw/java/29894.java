@BetaApi
  public final Address getAddress(ProjectRegionAddressName address) {

    GetAddressHttpRequest request =
        GetAddressHttpRequest.newBuilder()
            .setAddress(address == null ? null : address.toString())
            .build();
    return getAddress(request);
  }