function groupByDestructuring(variables, ignoreReadBeforeAssign) {
    const identifierMap = new Map();

    for (let i = 0; i < variables.length; ++i) {
        const variable = variables[i];
        const references = variable.references;
        const identifier = getIdentifierIfShouldBeConst(variable, ignoreReadBeforeAssign);
        let prevId = null;

        for (let j = 0; j < references.length; ++j) {
            const reference = references[j];
            const id = reference.identifier;

            /*
             * Avoid counting a reference twice or more for default values of
             * destructuring.
             */
            if (id === prevId) {
                continue;
            }
            prevId = id;

            // Add the identifier node into the destructuring group.
            const group = getDestructuringHost(reference);

            if (group) {
                if (identifierMap.has(group)) {
                    identifierMap.get(group).push(identifier);
                } else {
                    identifierMap.set(group, [identifier]);
                }
            }
        }
    }

    return identifierMap;
}