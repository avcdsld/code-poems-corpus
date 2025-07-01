function checkMethodAccessibilityModifier(methodDefinition) {
            if (
                !methodDefinition.accessibility &&
                util.isTypescript(context.getFilename())
            ) {
                context.report({
                    node: methodDefinition,
                    message:
                        "Missing accessibility modifier on method definition {{name}}.",
                    data: {
                        name: methodDefinition.key.name,
                    },
                });
            }
        }