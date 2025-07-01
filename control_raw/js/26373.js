function getPackageExportNames(packagePath) {
  const packageMeta = getPackageMeta(packagePath);
  const packageModulePath = path.join(packagePath, packageMeta.module);
  const moduleFileSource = fs.readFileSync(packageModulePath, "utf8");
  const { body } = esprima.parseModule(moduleFileSource);

  return body.reduce((result, statement) => {
    if (statement.type === "ExportDefaultDeclaration") {
      return result.concat(["default"]);
    }

    if (statement.type === "ExportNamedDeclaration") {
      return result.concat(getNamesFromDeclaration(statement));
    }

    return result;
  }, []);
}