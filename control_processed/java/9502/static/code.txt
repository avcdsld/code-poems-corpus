public void validate() throws GridConfigurationException {
    // validations occur here in the getters called on the configuration.
    try {
      configuration.getHubHost();
      configuration.getHubPort();
    } catch (RuntimeException e) {
      throw new GridConfigurationException(e.getMessage());
    }
  }