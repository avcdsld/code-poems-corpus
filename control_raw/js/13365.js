function getReadmeText(pkg) {
  const pkgDir = atPackagesDirectory().dir(pkg);
  const generatedDoc = pkgDir.read('./docs/docs.md');
  if (generatedDoc) pkgDir.write('Readme.md', generatedDoc);
  const text = pkgDir.read(README);
  if (text) return text;
  else return ''; // don't return "undefined"
}