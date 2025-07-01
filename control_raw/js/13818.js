function(name, options) {
  name = defaultValue(name, "Conditions");

  options = defaultValue(options, defaultValue.EMPTY_OBJECT);
  DisplayVariablesConcept.call(this, name, options);
}