@InternalApi
  public com.google.bigtable.admin.v2.CreateClusterRequest toProto(String projectId) {
    proto.setParent(NameUtil.formatInstanceName(projectId, instanceId));
    proto.getClusterBuilder().setLocation(NameUtil.formatLocationName(projectId, zone));

    return proto.build();
  }