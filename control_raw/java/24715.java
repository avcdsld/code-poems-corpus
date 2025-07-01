public URI getUri(final String name, final String defaultValue) {
    try {
      return getUri(name, new URI(defaultValue));
    } catch (final URISyntaxException e) {
      throw new IllegalArgumentException(e.getMessage());
    }
  }