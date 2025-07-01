function nodeSBindUpdate(node, sBind, changes, updater) {
    if (sBind) {
        var len = changes.length;

        while (len--) {
            if (changeExprCompare(changes[len].expr, sBind.value, node.scope)) {
                var newBindData = evalExpr(sBind.value, node.scope, node.owner);
                var keys = unionKeys(newBindData, node._sbindData);

                for (var i = 0, l = keys.length; i < l; i++) {
                    var key = keys[i];
                    var value = newBindData[key];

                    if (value !== node._sbindData[key]) {
                        updater(key, value);
                    }
                }

                node._sbindData = newBindData;
                break;
            }

        }
    }
}