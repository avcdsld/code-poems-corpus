public Actions dragAndDropBy(WebElement source, int xOffset, int yOffset) {
    if (isBuildingActions()) {
      action.addAction(new ClickAndHoldAction(jsonMouse, (Locatable) source));
      action.addAction(new MoveToOffsetAction(jsonMouse, null, xOffset, yOffset));
      action.addAction(new ButtonReleaseAction(jsonMouse, null));
    }

    return moveInTicks(source, 0, 0)
        .tick(defaultMouse.createPointerDown(LEFT.asArg()))
        .tick(defaultMouse.createPointerMove(Duration.ofMillis(250), Origin.pointer(), xOffset, yOffset))
        .tick(defaultMouse.createPointerUp(LEFT.asArg()));
  }