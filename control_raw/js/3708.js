function (node) {
                if (node.value && node.value.type === "FunctionExpression") {
                    if (node.key && node.key.type === "Identifier") {
                        _addResult(node.key);
                    }
                }
            }