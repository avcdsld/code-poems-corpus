public void registerApp(String appId, String shuffleSecret) {
    // Always put the new secret information to make sure it's the most up to date.
    // Otherwise we have to specifically look at the application attempt in addition
    // to the applicationId since the secrets change between application attempts on yarn.
    shuffleSecretMap.put(appId, shuffleSecret);
    logger.info("Registered shuffle secret for application {}", appId);
  }