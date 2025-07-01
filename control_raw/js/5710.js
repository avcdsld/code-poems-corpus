function findClosestParentOfType(node, types) {
            if (!node.parent) {
                return null;
            }
            if (types.indexOf(node.parent.type) === -1) {
                return findClosestParentOfType(node.parent, types);
            }
            return node.parent;
        }