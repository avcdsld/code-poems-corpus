function findGroup(catalogGroup, keywordsGroups, record) {
  for (var i = 0; i < keywordsGroups.length; i++) {
    var kg = keywordsGroups[i];
    var fields = record[kg.field];
    var matched = false;
    if (defined(fields)) {
      if (fields instanceof String || typeof fields === "string") {
        fields = [fields];
      }
      for (var j = 0; j < fields.length; j++) {
        var field = fields[j];
        if (matchValue(kg.value, field, kg.regex)) {
          matched = true;
          break;
        }
      }
    }
    if (matched) {
      var newGroup = addGroupIfNotAlreadyPresent(
        kg.group ? kg.group : kg.value,
        catalogGroup
      );
      if (kg.children && defined(newGroup)) {
        // recurse to see if it fits into any of the children
        catalogGroup = findGroup(newGroup, kg.children, record);
        if (!defined(catalogGroup)) {
          //console.log("No match in children for record "+record.title+"::"+record.subject+"::"+record.title+", will assign to "+newGroup.name);
          catalogGroup = newGroup;
        }
      } else if (defined(newGroup)) {
        catalogGroup = newGroup;
      }
      return catalogGroup;
    }
  }
}