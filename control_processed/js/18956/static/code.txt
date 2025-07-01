function isNodeWrapped(node, types) {
    var parents = getParents(node);
    var parentsTypes = parents.map(function(parent) {
        return parent.type;
    });
    return types.some(function(type) {
        return parentsTypes.some(function(parentType) {
            return parentType === type;
        });
    });
}