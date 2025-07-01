function reduceModifiers (previousValue, currentValue) {
    return previousValue + currentValue[property].replace(modifierPlaceholder, currentValue.className);
  }