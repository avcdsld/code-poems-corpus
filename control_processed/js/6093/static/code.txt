function same(a, b) {
    if (a.type !== b.type) {
        return false;
    }

    switch (a.type) {
        case "Identifier":
            return a.name === b.name;

        case "Literal":
            return a.value === b.value;

        case "MemberExpression": {
            const nameA = astUtils.getStaticPropertyName(a);

            // x.y = x["y"]
            if (nameA) {
                return (
                    same(a.object, b.object) &&
                    nameA === astUtils.getStaticPropertyName(b)
                );
            }

            /*
             * x[0] = x[0]
             * x[y] = x[y]
             * x.y = x.y
             */
            return (
                a.computed === b.computed &&
                same(a.object, b.object) &&
                same(a.property, b.property)
            );
        }

        case "ThisExpression":
            return true;

        default:
            return false;
    }
}