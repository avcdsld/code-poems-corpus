@Override
  public OperationHandle getColumns(SessionHandle sessionHandle,
      String catalogName, String schemaName, String tableName, String columnName)
          throws HiveSQLException {
    OperationHandle opHandle = sessionManager.getSession(sessionHandle)
        .getColumns(catalogName, schemaName, tableName, columnName);
    LOG.debug(sessionHandle + ": getColumns()");
    return opHandle;
  }