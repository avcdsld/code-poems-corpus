function blockScopeVarCheck(node, parent, grandParent) {
            if (!(/Function/u.test(grandParent.type) &&
                    parent.type === "BlockStatement" &&
                    isVarOnTop(node, parent.body))) {
                context.report({ node, messageId: "top" });
            }
        }