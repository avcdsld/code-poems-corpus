@Deprecated
  public List<SecurityReference> securityForPath(String path) {
    if (selector.test(path)) {
      return securityReferences;
    }
    return new ArrayList<SecurityReference>();
  }