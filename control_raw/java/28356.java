@BetaApi
  public final ListDiskTypesPagedResponse listDiskTypes(String zone) {
    ListDiskTypesHttpRequest request = ListDiskTypesHttpRequest.newBuilder().setZone(zone).build();
    return listDiskTypes(request);
  }