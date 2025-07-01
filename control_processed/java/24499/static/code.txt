@Override
  public void prefetchToken(final File tokenFile, final Props props, final Logger logger)
      throws HadoopSecurityManagerException {
    final String userToProxy = props.getString(JobProperties.USER_TO_PROXY);

    logger.info("Getting hadoop tokens based on props for " + userToProxy);
    doPrefetch(tokenFile, props, logger, userToProxy);
  }