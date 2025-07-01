public static ExpectedCondition<List<WebElement>> visibilityOfNestedElementsLocatedBy(
    final By parent,
    final By childLocator) {
    return new ExpectedCondition<List<WebElement>>() {

      @Override
      public List<WebElement> apply(WebDriver driver) {
        WebElement current = driver.findElement(parent);

        List<WebElement> allChildren = current.findElements(childLocator);
        // The original code only checked the first element. Fair enough.
        if (!allChildren.isEmpty() && allChildren.get(0).isDisplayed()) {
          return allChildren;
        }

        return null;
      }

      @Override
      public String toString() {
        return String.format("visibility of elements located by %s -> %s", parent, childLocator);
      }
    };
  }