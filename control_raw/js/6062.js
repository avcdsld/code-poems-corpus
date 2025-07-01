function report(node, loc, otherNode) {
            context.report({
                node,
                fix(fixer) {
                    if (options[loc]) {
                        if (loc === "before") {
                            return fixer.insertTextBefore(node, " ");
                        }
                        return fixer.insertTextAfter(node, " ");

                    }
                    let start, end;
                    const newText = "";

                    if (loc === "before") {
                        start = otherNode.range[1];
                        end = node.range[0];
                    } else {
                        start = node.range[1];
                        end = otherNode.range[0];
                    }

                    return fixer.replaceTextRange([start, end], newText);

                },
                messageId: options[loc] ? "missing" : "unexpected",
                data: {
                    loc
                }
            });
        }