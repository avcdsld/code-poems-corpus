function report(node, name, funcName, isProp) {
            let messageId;

            if (nameMatches === "always" && isProp) {
                messageId = "matchProperty";
            } else if (nameMatches === "always") {
                messageId = "matchVariable";
            } else if (isProp) {
                messageId = "notMatchProperty";
            } else {
                messageId = "notMatchVariable";
            }
            context.report({
                node,
                messageId,
                data: {
                    name,
                    funcName
                }
            });
        }