function checkConsistency(node, checkRedundancy) {

            // We are excluding getters/setters and spread properties as they are considered neither longform nor shorthand.
            const properties = node.properties.filter(canHaveShorthand);

            // Do we still have properties left after filtering the getters and setters?
            if (properties.length > 0) {
                const shorthandProperties = properties.filter(isShorthand);

                /*
                 * If we do not have an equal number of longform properties as
                 * shorthand properties, we are using the annotations inconsistently
                 */
                if (shorthandProperties.length !== properties.length) {

                    // We have at least 1 shorthand property
                    if (shorthandProperties.length > 0) {
                        context.report({ node, message: "Unexpected mix of shorthand and non-shorthand properties." });
                    } else if (checkRedundancy) {

                        /*
                         * If all properties of the object contain a method or value with a name matching it's key,
                         * all the keys are redundant.
                         */
                        const canAlwaysUseShorthand = properties.every(isRedundant);

                        if (canAlwaysUseShorthand) {
                            context.report({ node, message: "Expected shorthand for all properties." });
                        }
                    }
                }
            }
        }