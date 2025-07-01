public static ExpectedCondition<List<WebElement>> visibilityOfAllElements(
    final WebElement... elements) {
    return visibilityOfAllElements(Arrays.asList(elements));
  }