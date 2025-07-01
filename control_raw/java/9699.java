private static Executable locateFirefoxBinaryFromSystemProperty() {
    String binaryName = System.getProperty(FirefoxDriver.SystemProperty.BROWSER_BINARY);
    if (binaryName == null)
      return null;

    File binary = new File(binaryName);
    if (binary.exists() && !binary.isDirectory())
      return new Executable(binary);

    Platform current = Platform.getCurrent();
    if (current.is(WINDOWS)) {
      if (!binaryName.endsWith(".exe")) {
        binaryName += ".exe";
      }

    } else if (current.is(MAC)) {
      if (!binaryName.endsWith(".app")) {
        binaryName += ".app";
      }
      binaryName += "/Contents/MacOS/firefox-bin";
    }

    binary = new File(binaryName);
    if (binary.exists())
      return new Executable(binary);

    throw new WebDriverException(
      String.format("'%s' property set, but unable to locate the requested binary: %s",
                    FirefoxDriver.SystemProperty.BROWSER_BINARY, binaryName));
  }