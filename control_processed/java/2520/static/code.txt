@Override
  public OperationHandle getSchemas(SessionHandle sessionHandle, String catalogName,
      String schemaName) throws HiveSQLException {
    return cliService.getSchemas(sessionHandle, catalogName, schemaName);
  }