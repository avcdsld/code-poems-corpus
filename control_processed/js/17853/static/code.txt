function expandQNames(xpath) {
  var namespaces = constants.XmlNamespaces;
  var pathParts = xpath.split('/');
  for (var i=0; i < pathParts.length; i++) {
    if (pathParts[i].indexOf(':') !== -1) {
      var QNameParts = pathParts[i].split(':');
      if (QNameParts.length !== 2) {
        throw new Error('Unable to parse XPath string : ' + xpath + ' : with QName : ' + pathParts[i]);
      }
      var expandedPath = XPATH_PATH_TEMPLATE.replace('LOCAL_NAME', QNameParts[1]);
      expandedPath = expandedPath.replace('NAMESPACE', namespaces[QNameParts[0]]);
      pathParts[i] = expandedPath;
    }
  }
  return pathParts.join('/');
}