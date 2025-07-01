@BetaApi
  public final AggregatedListInstancesPagedResponse aggregatedListInstances(ProjectName project) {
    AggregatedListInstancesHttpRequest request =
        AggregatedListInstancesHttpRequest.newBuilder()
            .setProject(project == null ? null : project.toString())
            .build();
    return aggregatedListInstances(request);
  }