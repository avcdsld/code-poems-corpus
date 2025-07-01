public final Operation deleteCluster(String projectId, String zone, String clusterId) {

    DeleteClusterRequest request =
        DeleteClusterRequest.newBuilder()
            .setProjectId(projectId)
            .setZone(zone)
            .setClusterId(clusterId)
            .build();
    return deleteCluster(request);
  }