public final Intent getIntent(IntentName name, String languageCode) {

    GetIntentRequest request =
        GetIntentRequest.newBuilder()
            .setName(name == null ? null : name.toString())
            .setLanguageCode(languageCode)
            .build();
    return getIntent(request);
  }