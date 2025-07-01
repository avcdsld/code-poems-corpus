function createRegexDeserializer(fieldName) {
  return function(catalogMember, json, propertyName, options) {
    if (defined(json[fieldName])) {
      catalogMember[fieldName] = new RegExp(json[fieldName], "i");
    }
  };
}