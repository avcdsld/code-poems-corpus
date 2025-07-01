public static ExpectedCondition<Boolean> urlMatches(final String regex) {
    return new ExpectedCondition<Boolean>() {
      private String currentUrl;
      private Pattern pattern;
      private Matcher matcher;

      @Override
      public Boolean apply(WebDriver driver) {
        currentUrl = driver.getCurrentUrl();
        pattern = Pattern.compile(regex);
        matcher = pattern.matcher(currentUrl);
        return matcher.find();
      }

      @Override
      public String toString() {
        return String
          .format("url to match the regex \"%s\". Current url: \"%s\"", regex, currentUrl);
      }
    };
  }