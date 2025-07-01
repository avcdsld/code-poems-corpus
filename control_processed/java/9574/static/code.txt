public Actions sendKeys(CharSequence... keys) {
    if (isBuildingActions()) {
      action.addAction(new SendKeysAction(jsonKeyboard, jsonMouse, null, keys));
    }

    return sendKeysInTicks(keys);
  }