function getIdentifierForArgumentValue(value: ArgumentValue): mixed {
  switch (value.kind) {
    case 'Variable':
      return {variable: value.variableName};
    case 'Literal':
      return {value: value.value};
    case 'ListValue':
      return {
        list: value.items.map(item => getIdentifierForArgumentValue(item)),
      };
    case 'ObjectValue':
      return {
        object: value.fields.map(field => ({
          name: field.name,
          value: getIdentifierForArgumentValue(field.value),
        })),
      };
    default:
      invariant(
        false,
        'getIdentifierForArgumentValue(): Unsupported AST kind `%s`.',
        value.kind,
      );
  }
}