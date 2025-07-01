function isBlockNode(node) {
        return node &&
            ((node.nodeType == 1 && !/^(inline(-block|-table)?|none)$/.test(getComputedDisplay(node))) ||
            node.nodeType == 9 || node.nodeType == 11);
    }