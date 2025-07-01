public final ProductSet getProductSet(String name) {

    GetProductSetRequest request = GetProductSetRequest.newBuilder().setName(name).build();
    return getProductSet(request);
  }