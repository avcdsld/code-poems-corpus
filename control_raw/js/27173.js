function parseVariableDeclarations(string) {

  // Do not parse empty files. Otherwise gonzales.parse will fail
  if (!string) {
    return [];
  }

  var out = [],
      ast = gonzales.parse(string, {
        syntax: 'less'
      });
  // Exclude functions arguments
  ast.traverse(function(node, index, parent) {
    if (node.is('arguments')) {
      parent.removeChild(index);
    }
  });
  ast.traverseByType('declaration', function(decl) {
    // Only consider @variable: value declarations
    var varName,
        varFullName,
        varVal = '',
        varLine = 1;
    decl.traverseByType('variable', function(varNode) {
      varName = varNode.content.toString();
      varFullName = varNode.toString();
      decl.traverseByType('value', function(valNode) {
        varVal = valNode.toString();
        varLine = valNode.start.line;
      });
      if (varFullName !== varVal) {
        out.push({
          name: varName,
          value: varVal.trim(),
          line: varLine
        });
      }
    });
  });
  return out;
}