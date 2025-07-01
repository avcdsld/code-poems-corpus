function globalizeDeclaration(node, bindings) {
  return node.declarations.map(declaration =>
    t.expressionStatement(
      t.assignmentExpression(
        "=",
        getAssignmentTarget(declaration.id, bindings),
        declaration.init || t.unaryExpression("void", t.numericLiteral(0))
      )
    )
  );
}