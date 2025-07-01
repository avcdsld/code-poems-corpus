function checkASTandFunction(ast, astName, func, functionName) {
  typeCheckObject(ast, astName);
  typeCheckFunction(func, functionName);
  runValidator(ast, astName);
}