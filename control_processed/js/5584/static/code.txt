function report(nodeOrToken) {
            context.report({
                node: nodeOrToken,
                messageId: "unexpected",
                fix(fixer) {

                    /*
                     * Expand the replacement range to include the surrounding
                     * tokens to avoid conflicting with semi.
                     * https://github.com/eslint/eslint/issues/7928
                     */
                    return new FixTracker(fixer, context.getSourceCode())
                        .retainSurroundingTokens(nodeOrToken)
                        .remove(nodeOrToken);
                }
            });
        }