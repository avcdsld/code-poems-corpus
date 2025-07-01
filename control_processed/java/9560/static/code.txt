public String runHTMLSuite(
    String browser,
    String startURL,
    String suiteURL,
    File outputFile,
    long timeoutInSeconds,
    String userExtensions) throws IOException {
    File parent = outputFile.getParentFile();
    if (parent != null && !parent.exists()) {
      parent.mkdirs();
    }
    if (outputFile.exists() && !outputFile.canWrite()) {
      throw new IOException("Can't write to outputFile: " + outputFile.getAbsolutePath());
    }
    long timeoutInMs = 1000L * timeoutInSeconds;
    if (timeoutInMs < 0) {
      log.warning("Looks like the timeout overflowed, so resetting it to the maximum.");
      timeoutInMs = Long.MAX_VALUE;
    }

    WebDriver driver = null;
    try {
      driver = createDriver(browser);
      URL suiteUrl = determineSuiteUrl(startURL, suiteURL);

      driver.get(suiteUrl.toString());
      Selenium selenium = new WebDriverBackedSelenium(driver, startURL);
      selenium.setTimeout(String.valueOf(timeoutInMs));
      if (userExtensions != null) {
        selenium.setExtensionJs(userExtensions);
      }
      List<WebElement> allTables = driver.findElements(By.id("suiteTable"));
      if (allTables.isEmpty()) {
        throw new RuntimeException("Unable to find suite table: " + driver.getPageSource());
      }
      Results results = new CoreTestSuite(suiteUrl.toString()).run(driver, selenium, new URL(startURL));

      HTMLTestResults htmlResults = results.toSuiteResult();
      try (Writer writer = Files.newBufferedWriter(outputFile.toPath())) {
        htmlResults.write(writer);
      }

      return results.isSuccessful() ? "PASSED" : "FAILED";
    } finally {
      if (server != null) {
        try {
          server.stop();
        } catch (Exception e) {
          // Nothing sane to do. Log the error and carry on
          log.log(Level.INFO, "Exception shutting down server. You may ignore this.", e);
        }
      }

      if (driver != null) {
        driver.quit();
      }
    }
  }