function getDestructuringHost(reference) {
    if (!reference.isWrite()) {
        return null;
    }
    let node = reference.identifier.parent;

    while (PATTERN_TYPE.test(node.type)) {
        node = node.parent;
    }

    if (!DESTRUCTURING_HOST_TYPE.test(node.type)) {
        return null;
    }
    return node;
}