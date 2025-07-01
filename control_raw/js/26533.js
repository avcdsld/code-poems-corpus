function validateName(node) {
            const name = node.key.name;
            const accessibility = node.accessibility || "public";
            const convention = conventions[accessibility];

            if (!convention || convention.test(name)) return;

            context.report({
                node: node.key,
                message:
                    "{{accessibility}} property {{name}} should match {{convention}}.",
                data: { accessibility, name, convention },
            });
        }