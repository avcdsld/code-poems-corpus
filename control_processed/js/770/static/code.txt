function addonsManager_getViews(aSpec) {
    var spec = aSpec || { };
    var attribute = spec.attribute;
    var value = spec.value;

    return this.getElements({type: "views", subtype: attribute, value: value});
  }