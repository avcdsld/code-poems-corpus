function addTypeDeps(deps) {
  const packagesWithDTPackage = Object.keys(deps).filter(
    name => packagesWithBundledTypes.indexOf(name) === -1,
  );

  packagesWithDTPackage.forEach(name => {
    let resolvedName = name;
    // scoped package?
    if (name.startsWith('@')) {
      // https://github.com/DefinitelyTyped/DefinitelyTyped#what-about-scoped-packages
      resolvedName = name.slice(1).replace('/', '__');
    }

    deps[`@types/${resolvedName}`] = 'latest';
  });

  return deps;
}