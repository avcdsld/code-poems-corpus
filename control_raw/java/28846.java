@BetaApi
  public final Operation setTagsInstance(String instance, Tags tagsResource) {

    SetTagsInstanceHttpRequest request =
        SetTagsInstanceHttpRequest.newBuilder()
            .setInstance(instance)
            .setTagsResource(tagsResource)
            .build();
    return setTagsInstance(request);
  }