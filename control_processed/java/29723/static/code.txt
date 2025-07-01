@SuppressWarnings("WeakerAccess")
  public ApiFuture<Void> awaitReplicationAsync(final String tableId) {
    // TODO(igorbernstein2): remove usage of trypesafe names
    com.google.bigtable.admin.v2.TableName tableName =
        com.google.bigtable.admin.v2.TableName.of(projectId, instanceId, tableId);
    return stub.awaitReplicationCallable().futureCall(tableName);
  }