function checkCallNew(node) {
            const callee = node.callee;

            if (hasExcessParens(callee) && precedence(callee) >= precedence(node)) {
                const hasNewParensException = callee.type === "NewExpression" && !isNewExpressionWithParens(callee);

                if (
                    hasDoubleExcessParens(callee) ||
                    !isIIFE(node) && !hasNewParensException && !(

                        /*
                         * Allow extra parens around a new expression if
                         * there are intervening parentheses.
                         */
                        (callee.type === "MemberExpression" && doesMemberExpressionContainCallExpression(callee))
                    )
                ) {
                    report(node.callee);
                }
            }
            if (node.arguments.length === 1) {
                if (hasDoubleExcessParens(node.arguments[0]) && precedence(node.arguments[0]) >= PRECEDENCE_OF_ASSIGNMENT_EXPR) {
                    report(node.arguments[0]);
                }
            } else {
                node.arguments
                    .filter(arg => hasExcessParens(arg) && precedence(arg) >= PRECEDENCE_OF_ASSIGNMENT_EXPR)
                    .forEach(report);
            }
        }