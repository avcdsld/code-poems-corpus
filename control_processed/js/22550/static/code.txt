async function makeDocumentableObject(folder) {
  const fullPath = path.join(REACT_MD_JS, folder);
  const contents = await readFile(path.join(fullPath, 'index.js'), 'UTF-8');

  const components = contents.split(/\r?\n/).reduce((exports, line) => {
    // go line-by-line in the src/js/SECTION/index.js file to get a list of the exported
    // components in this section
    if (line.match(/export/)) {
      const component = line.replace(/export (default |{ )?(\w+).*/, '$2');
      if (exports.indexOf(component) === -1 && DEPRECATED.indexOf(component) === -1 && component.indexOf('FakeInked') === -1) {
        exports.push(component);
      }
    }

    return exports;
  }, []);

  return { folder, components, fullPath };
}