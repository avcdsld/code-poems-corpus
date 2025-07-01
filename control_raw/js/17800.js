function isReactCreateClassCallModular(path: NodePath): boolean {
  if (t.ExpressionStatement.check(path.node)) {
    path = path.get('expression');
  }

  if (!match(path.node, { type: 'CallExpression' })) {
    return false;
  }
  const module = resolveToModule(path);
  return Boolean(module && module === 'create-react-class');
}