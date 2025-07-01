public final ListCryptoKeyVersionsPagedResponse listCryptoKeyVersions(CryptoKeyName parent) {
    ListCryptoKeyVersionsRequest request =
        ListCryptoKeyVersionsRequest.newBuilder()
            .setParent(parent == null ? null : parent.toString())
            .build();
    return listCryptoKeyVersions(request);
  }