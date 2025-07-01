@Override
  public GetInfoValue getInfo(SessionHandle sessionHandle, GetInfoType getInfoType)
      throws HiveSQLException {
    return cliService.getInfo(sessionHandle, getInfoType);
  }