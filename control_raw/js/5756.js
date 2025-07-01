function checkForLoops(node) {
            const loopNode = getContainingLoopNode(node);

            if (!loopNode) {
                return;
            }

            const references = context.getScope().through;
            const unsafeRefs = references.filter(r => !isSafe(loopNode, r)).map(r => r.identifier.name);

            if (unsafeRefs.length > 0) {
                context.report({
                    node,
                    messageId: "unsafeRefs",
                    data: { varNames: `'${unsafeRefs.join("', '")}'` }
                });
            }
        }