function checkFunction(node) {
            const functionConfig = getConfigForFunction(node);

            if (functionConfig === "ignore") {
                return;
            }

            const rightToken = sourceCode.getFirstToken(node, astUtils.isOpeningParenToken);
            const leftToken = sourceCode.getTokenBefore(rightToken);
            const hasSpacing = sourceCode.isSpaceBetweenTokens(leftToken, rightToken);

            if (hasSpacing && functionConfig === "never") {
                context.report({
                    node,
                    loc: leftToken.loc.end,
                    message: "Unexpected space before function parentheses.",
                    fix: fixer => fixer.removeRange([leftToken.range[1], rightToken.range[0]])
                });
            } else if (!hasSpacing && functionConfig === "always") {
                context.report({
                    node,
                    loc: leftToken.loc.end,
                    message: "Missing space before function parentheses.",
                    fix: fixer => fixer.insertTextAfter(leftToken, " ")
                });
            }
        }