function markVariableAsUsed(context, name) {
  let scope = context.getScope();
  let variables;
  let i;
  let len;
  let found = false;

  // Special Node.js scope means we need to start one level deeper
  if (scope.type === 'global') {
    while (scope.childScopes.length) {
      scope = scope.childScopes[0];
    }
  }

  do {
    variables = scope.variables;
    for (i = 0, len = variables.length; i < len; i++) { // eslint-disable-line no-plusplus
      if (variables[i].name === name) {
        variables[i].eslintUsed = true;
        found = true;
      }
    }
    scope = scope.upper;
  } while (scope);

  return found;
}