function enterFunctionInFunctionMode(node, useStrictDirectives) {
            const isInClass = classScopes.length > 0,
                isParentGlobal = scopes.length === 0 && classScopes.length === 0,
                isParentStrict = scopes.length > 0 && scopes[scopes.length - 1],
                isStrict = useStrictDirectives.length > 0;

            if (isStrict) {
                if (!isSimpleParameterList(node.params)) {
                    context.report({ node: useStrictDirectives[0], messageId: "nonSimpleParameterList" });
                } else if (isParentStrict) {
                    context.report({ node: useStrictDirectives[0], messageId: "unnecessary", fix: getFixFunction(useStrictDirectives[0]) });
                } else if (isInClass) {
                    context.report({ node: useStrictDirectives[0], messageId: "unnecessaryInClasses", fix: getFixFunction(useStrictDirectives[0]) });
                }

                reportAllExceptFirst(useStrictDirectives, "multiple", true);
            } else if (isParentGlobal) {
                if (isSimpleParameterList(node.params)) {
                    context.report({ node, messageId: "function" });
                } else {
                    context.report({
                        node,
                        messageId: "wrap",
                        data: { name: astUtils.getFunctionNameWithKind(node) }
                    });
                }
            }

            scopes.push(isParentStrict || isStrict);
        }