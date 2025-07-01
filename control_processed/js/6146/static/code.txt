function checkBinaryLogical(node) {
            const prec = precedence(node);
            const leftPrecedence = precedence(node.left);
            const rightPrecedence = precedence(node.right);
            const isExponentiation = node.operator === "**";
            const shouldSkipLeft = (NESTED_BINARY && (node.left.type === "BinaryExpression" || node.left.type === "LogicalExpression")) ||
              node.left.type === "UnaryExpression" && isExponentiation;
            const shouldSkipRight = NESTED_BINARY && (node.right.type === "BinaryExpression" || node.right.type === "LogicalExpression");

            if (!shouldSkipLeft && hasExcessParens(node.left) && (leftPrecedence > prec || (leftPrecedence === prec && !isExponentiation))) {
                report(node.left);
            }
            if (!shouldSkipRight && hasExcessParens(node.right) && (rightPrecedence > prec || (rightPrecedence === prec && isExponentiation))) {
                report(node.right);
            }
        }