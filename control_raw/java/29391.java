public final KeyRing getKeyRing(KeyRingName name) {

    GetKeyRingRequest request =
        GetKeyRingRequest.newBuilder().setName(name == null ? null : name.toString()).build();
    return getKeyRing(request);
  }