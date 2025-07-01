@BetaApi
  public final Operation insertUrlMap(String project, UrlMap urlMapResource) {

    InsertUrlMapHttpRequest request =
        InsertUrlMapHttpRequest.newBuilder()
            .setProject(project)
            .setUrlMapResource(urlMapResource)
            .build();
    return insertUrlMap(request);
  }