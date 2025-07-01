function getVisitorKeys(visitorKeys, node) {
    let keys = visitorKeys[node.type];

    if (!keys) {
        keys = vk.getKeys(node);
        debug("Unknown node type \"%s\": Estimated visitor keys %j", node.type, keys);
    }

    return keys;
}