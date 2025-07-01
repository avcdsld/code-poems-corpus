function isNumeric(value) {
  if (_.isNumber(value)) {
    return true;
  }
  if (_.isString(value)) {
    if (!isFinite(value)) {
      return false;
    }
    // str is a finite number, but not all number strings should be numbers
    // If the string starts with 0, is more than 1 character, and does not have a period, it should stay a string
    // It could be an account number for example
    if (value[0] === '0' && value.length > 1 && value.indexOf('.') === -1) {
      return false;
    }

    return true;
  }
  return false;
}