function transformTypeImport(path, state) {
    var source = path.get('source');
    if (source.type === 'StringLiteral') {
      var module = mapModule(state, source.node.value);
      if (module) {
        source.replaceWith(t.stringLiteral(module));
      }
    }
  }