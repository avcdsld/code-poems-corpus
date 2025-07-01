public static ExpectedCondition<WebElement> elementToBeClickable(final WebElement element) {
    return new ExpectedCondition<WebElement>() {

      @Override
      public WebElement apply(WebDriver driver) {
        WebElement visibleElement = visibilityOf(element).apply(driver);
        try {
          if (visibleElement != null && visibleElement.isEnabled()) {
            return visibleElement;
          }
          return null;
        } catch (StaleElementReferenceException e) {
          return null;
        }
      }

      @Override
      public String toString() {
        return "element to be clickable: " + element;
      }
    };
  }