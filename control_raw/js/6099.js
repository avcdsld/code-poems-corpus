function reportIfEmpty(node) {
            const kind = getKind(node);
            const name = astUtils.getFunctionNameWithKind(node);
            const innerComments = sourceCode.getTokens(node.body, {
                includeComments: true,
                filter: astUtils.isCommentToken
            });

            if (allowed.indexOf(kind) === -1 &&
                node.body.type === "BlockStatement" &&
                node.body.body.length === 0 &&
                innerComments.length === 0
            ) {
                context.report({
                    node,
                    loc: node.body.loc.start,
                    messageId: "unexpected",
                    data: { name }
                });
            }
        }