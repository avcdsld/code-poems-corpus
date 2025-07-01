function checkForCreateNode(id, name, type, props, children) {
  typeCheckInteger(id, 'id');
  typeCheckString(name, 'name');
  checkNodeType(type);
  checkProps(props);
  checkChildren(children);
}