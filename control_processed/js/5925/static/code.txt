function isPropertyDescriptor(node) {

    // Object.defineProperty(obj, "foo", {set: ...})
    if (isArgumentOfMethodCall(node, 2, "Object", "defineProperty") ||
        isArgumentOfMethodCall(node, 2, "Reflect", "defineProperty")
    ) {
        return true;
    }

    /*
     * Object.defineProperties(obj, {foo: {set: ...}})
     * Object.create(proto, {foo: {set: ...}})
     */
    const grandparent = node.parent.parent;

    return grandparent.type === "ObjectExpression" && (
        isArgumentOfMethodCall(grandparent, 1, "Object", "create") ||
        isArgumentOfMethodCall(grandparent, 1, "Object", "defineProperties")
    );
}