function removePropValue(node, name) {
    var propInfo = properties.hasOwnProperty(name) && properties[name];
    if (propInfo) {
        if (propInfo.mustUseProperty) {
            var propName = propInfo.propertyName;
            if (propInfo.hasBooleanValue) {
                node[propName] = false;
            } else {
                node[propName] = '';
            }
        } else {
            node.removeAttribute(propInfo.attributeName);
        }
    } else if (isCustomAttribute(name)) {
        node.removeAttribute(name);
    }
}