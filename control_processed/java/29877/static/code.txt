@BetaApi
  public final Operation moveDiskProject(
      ProjectName project, DiskMoveRequest diskMoveRequestResource) {

    MoveDiskProjectHttpRequest request =
        MoveDiskProjectHttpRequest.newBuilder()
            .setProject(project == null ? null : project.toString())
            .setDiskMoveRequestResource(diskMoveRequestResource)
            .build();
    return moveDiskProject(request);
  }