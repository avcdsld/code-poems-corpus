function getAliases(obj) {
  var names = {};
  if (obj.name) {
    names[obj.name] = true;
  }
  var aliases = obj.aliases;
  var i, l;
  for (i = 0, l = aliases.length; i < l; i++) {
    names[aliases[i]] = true;
  }
  return Object.keys(names);
}