function addActionCreator(path, actionMap, filePath) {

  const {node, parentPath} = path;
  if (node.arguments.length && parentPath.node && parentPath.node.id) {

    const action = parentPath.node.id.name;
    const firstArg = node.arguments[0];
    const actionType = firstArg.property ? firstArg.property.name : firstArg.name;

    const {loc} = parentPath.node
    actionMap[actionType] = actionMap[actionType] || createActionNode(actionType);
    actionMap[actionType].action = {name: action, path: `${filePath}#L${loc.start.line}-L${loc.end.line}`};
  }
}