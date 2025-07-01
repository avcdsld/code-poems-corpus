function report(node, needed, gottenSpaces, gottenTabs, loc, isLastNodeCheck) {
            if (gottenSpaces && gottenTabs) {

                // To avoid conflicts with `no-mixed-spaces-and-tabs`, don't report lines that have both spaces and tabs.
                return;
            }

            const desiredIndent = (indentType === "space" ? " " : "\t").repeat(needed);

            const textRange = isLastNodeCheck
                ? [node.range[1] - node.loc.end.column, node.range[1] - node.loc.end.column + gottenSpaces + gottenTabs]
                : [node.range[0] - node.loc.start.column, node.range[0] - node.loc.start.column + gottenSpaces + gottenTabs];

            context.report({
                node,
                loc,
                messageId: "expected",
                data: createErrorMessageData(needed, gottenSpaces, gottenTabs),
                fix: fixer => fixer.replaceTextRange(textRange, desiredIndent)
            });
        }