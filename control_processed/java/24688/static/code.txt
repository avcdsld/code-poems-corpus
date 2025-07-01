public static int validate(final String jobName, final Props serverProps, final Props jobProps,
      final Collection<String> errors) {
    final int maxNumCallback =
        serverProps.getInt(
            JobCallbackConstants.MAX_CALLBACK_COUNT_PROPERTY_KEY,
            JobCallbackConstants.DEFAULT_MAX_CALLBACK_COUNT);

    final int maxPostBodyLength =
        serverProps.getInt(MAX_POST_BODY_LENGTH_PROPERTY_KEY,
            DEFAULT_POST_BODY_LENGTH);

    int totalCallbackCount = 0;
    for (final JobCallbackStatusEnum jobStatus : JobCallbackStatusEnum.values()) {
      totalCallbackCount +=
          validateBasedOnStatus(jobProps, errors, jobStatus, maxNumCallback,
              maxPostBodyLength);
    }

    if (logger.isDebugEnabled()) {
      logger.debug("Found " + totalCallbackCount + " job callbacks for job "
          + jobName);
    }
    return totalCallbackCount;
  }