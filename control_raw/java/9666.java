public TouchActions singleTap(WebElement onElement) {
    if (touchScreen != null) {
      action.addAction(new SingleTapAction(touchScreen, (Locatable) onElement));
    }
    tick(touchPointer.createPointerDown(0));
    tick(touchPointer.createPointerUp(0));
    return this;
  }