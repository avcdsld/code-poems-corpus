function nextRight(node) {
    var children = node.children;
    return children.length && node.isExpand ? children[children.length - 1] : node.hierNode.thread;
}