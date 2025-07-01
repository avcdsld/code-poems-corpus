static ManagedChannelServiceConfig fromServiceConfig(
      Map<String, ?> serviceConfig,
      boolean retryEnabled,
      int maxRetryAttemptsLimit,
      int maxHedgedAttemptsLimit,
      @Nullable Object loadBalancingConfig) {
    Throttle retryThrottling = null;
    if (retryEnabled) {
      retryThrottling = ServiceConfigUtil.getThrottlePolicy(serviceConfig);
    }
    Map<String, MethodInfo> serviceMethodMap = new HashMap<>();
    Map<String, MethodInfo> serviceMap = new HashMap<>();

    // Try and do as much validation here before we swap out the existing configuration.  In case
    // the input is invalid, we don't want to lose the existing configuration.
    List<Map<String, ?>> methodConfigs =
        ServiceConfigUtil.getMethodConfigFromServiceConfig(serviceConfig);

    if (methodConfigs == null) {
      // this is surprising, but possible.
      return new ManagedChannelServiceConfig(
          serviceMethodMap, serviceMap, retryThrottling, loadBalancingConfig);
    }

    for (Map<String, ?> methodConfig : methodConfigs) {
      MethodInfo info = new MethodInfo(
          methodConfig, retryEnabled, maxRetryAttemptsLimit, maxHedgedAttemptsLimit);

      List<Map<String, ?>> nameList =
          ServiceConfigUtil.getNameListFromMethodConfig(methodConfig);

      checkArgument(
          nameList != null && !nameList.isEmpty(), "no names in method config %s", methodConfig);
      for (Map<String, ?> name : nameList) {
        String serviceName = ServiceConfigUtil.getServiceFromName(name);
        checkArgument(!Strings.isNullOrEmpty(serviceName), "missing service name");
        String methodName = ServiceConfigUtil.getMethodFromName(name);
        if (Strings.isNullOrEmpty(methodName)) {
          // Service scoped config
          checkArgument(
              !serviceMap.containsKey(serviceName), "Duplicate service %s", serviceName);
          serviceMap.put(serviceName, info);
        } else {
          // Method scoped config
          String fullMethodName = MethodDescriptor.generateFullMethodName(serviceName, methodName);
          checkArgument(
              !serviceMethodMap.containsKey(fullMethodName),
              "Duplicate method name %s",
              fullMethodName);
          serviceMethodMap.put(fullMethodName, info);
        }
      }
    }

    return new ManagedChannelServiceConfig(
        serviceMethodMap, serviceMap, retryThrottling, loadBalancingConfig);
  }