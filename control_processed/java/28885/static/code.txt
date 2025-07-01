public final GenerateIdTokenResponse generateIdToken(
      ServiceAccountName name, List<String> delegates, String audience, boolean includeEmail) {

    GenerateIdTokenRequest request =
        GenerateIdTokenRequest.newBuilder()
            .setName(name == null ? null : name.toString())
            .addAllDelegates(delegates)
            .setAudience(audience)
            .setIncludeEmail(includeEmail)
            .build();
    return generateIdToken(request);
  }