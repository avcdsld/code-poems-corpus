public static void filterAdminOnlyFlowParams(final UserManager userManager,
      final ExecutionOptions options, final User user) throws ExecutorManagerException {
    if (options == null || options.getFlowParameters() == null) {
      return;
    }

    final Map<String, String> params = options.getFlowParameters();
    // is azkaban Admin
    if (!hasPermission(userManager, user, Type.ADMIN)) {
      params.remove(ExecutionOptions.FLOW_PRIORITY);
      params.remove(ExecutionOptions.USE_EXECUTOR);
    } else {
      validateIntegerParam(params, ExecutionOptions.FLOW_PRIORITY);
      validateIntegerParam(params, ExecutionOptions.USE_EXECUTOR);
    }
  }