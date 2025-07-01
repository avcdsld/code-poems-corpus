function normalizeOptions(options) {
    const isNodeSpecificOption = lodash.overSome([lodash.isPlainObject, lodash.isString]);

    if (lodash.isPlainObject(options) && lodash.some(options, isNodeSpecificOption)) {
        return {
            ObjectExpression: normalizeOptionValue(options.ObjectExpression),
            ObjectPattern: normalizeOptionValue(options.ObjectPattern),
            ImportDeclaration: normalizeOptionValue(options.ImportDeclaration),
            ExportNamedDeclaration: normalizeOptionValue(options.ExportDeclaration)
        };
    }

    const value = normalizeOptionValue(options);

    return { ObjectExpression: value, ObjectPattern: value, ImportDeclaration: value, ExportNamedDeclaration: value };
}