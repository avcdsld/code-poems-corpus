private static Resource getAutoDetectedResourceType() {
    if (System.getenv("GAE_INSTANCE") != null) {
      return Resource.GaeAppFlex;
    }
    if (System.getenv("KUBERNETES_SERVICE_HOST") != null) {
      return Resource.Container;
    }
    if (ServiceOptions.getAppEngineAppId() != null) {
      return Resource.GaeAppStandard;
    }
    if (MetadataConfig.getInstanceId() != null) {
      return Resource.GceInstance;
    }
    // default Resource type
    return Resource.Global;
  }