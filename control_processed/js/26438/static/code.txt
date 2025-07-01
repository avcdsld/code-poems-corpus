function setPropValue(node, name, value) {
    var propInfo = properties.hasOwnProperty(name) && properties[name];
    if (propInfo) {
        // should delete value from dom
        if (value == null || propInfo.hasBooleanValue && !value || propInfo.hasNumericValue && isNaN(value) || propInfo.hasPositiveNumericValue && value < 1 || propInfo.hasOverloadedBooleanValue && value === false) {
            removePropValue(node, name);
        } else if (propInfo.mustUseProperty) {
            node[propInfo.propertyName] = value;
        } else {
            var attributeName = propInfo.attributeName;
            var namespace = propInfo.attributeNamespace;

            // `setAttribute` with objects becomes only `[object]` in IE8/9,
            // ('' + value) makes it output the correct toString()-value.
            if (namespace) {
                node.setAttributeNS(namespace, attributeName, '' + value);
            } else if (propInfo.hasBooleanValue || propInfo.hasOverloadedBooleanValue && value === true) {
                node.setAttribute(attributeName, '');
            } else {
                node.setAttribute(attributeName, '' + value);
            }
        }
    } else if (isCustomAttribute(name) && VALID_ATTRIBUTE_NAME_REGEX.test(name)) {
        if (value == null) {
            node.removeAttribute(name);
        } else {
            node.setAttribute(name, '' + value);
        }
    }
}