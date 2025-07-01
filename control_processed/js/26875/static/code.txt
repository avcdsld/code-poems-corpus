function getModuleRequirePath(moduleName) {
  return moduleName[0] === '.' ?
    require.resolve(resolve(process.cwd(), moduleName)) :
    moduleName
}