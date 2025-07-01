@SuppressWarnings("WeakerAccess")
  public ApiFuture<Cluster> getClusterAsync(String instanceId, String clusterId) {
    String name = NameUtil.formatClusterName(projectId, instanceId, clusterId);

    com.google.bigtable.admin.v2.GetClusterRequest request =
        com.google.bigtable.admin.v2.GetClusterRequest.newBuilder().setName(name).build();

    return ApiFutures.transform(
        stub.getClusterCallable().futureCall(request),
        new ApiFunction<com.google.bigtable.admin.v2.Cluster, Cluster>() {
          @Override
          public Cluster apply(com.google.bigtable.admin.v2.Cluster proto) {
            return Cluster.fromProto(proto);
          }
        },
        MoreExecutors.directExecutor());
  }