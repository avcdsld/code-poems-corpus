function arrayOfTypeValidation(validator) {
  return withRequired(function arrayOfType(value) {
    if (!Array.isArray(value)) {
      throw `Value ${value} must be an array.`;
    }
    value.every(validator);
  });
}