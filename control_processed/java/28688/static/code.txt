@BetaApi
  public final Operation insertInterconnect(
      ProjectName project, Interconnect interconnectResource) {

    InsertInterconnectHttpRequest request =
        InsertInterconnectHttpRequest.newBuilder()
            .setProject(project == null ? null : project.toString())
            .setInterconnectResource(interconnectResource)
            .build();
    return insertInterconnect(request);
  }