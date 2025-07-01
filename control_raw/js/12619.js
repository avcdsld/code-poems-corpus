function nodeSBindInit(node, sBind) {
    if (sBind && node.scope) {
        node._sbindData = evalExpr(sBind.value, node.scope, node.owner);
        return true;
    }
}