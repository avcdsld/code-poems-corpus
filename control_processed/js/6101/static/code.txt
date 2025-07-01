function exitLabeledScope(node) {
            if (!scopeInfo.used) {
                context.report({
                    node: node.label,
                    messageId: "unused",
                    data: node.label,
                    fix(fixer) {

                        /*
                         * Only perform a fix if there are no comments between the label and the body. This will be the case
                         * when there is exactly one token/comment (the ":") between the label and the body.
                         */
                        if (sourceCode.getTokenAfter(node.label, { includeComments: true }) ===
                                sourceCode.getTokenBefore(node.body, { includeComments: true })) {
                            return fixer.removeRange([node.range[0], node.body.range[0]]);
                        }

                        return null;
                    }
                });
            }

            scopeInfo = scopeInfo.upper;
        }