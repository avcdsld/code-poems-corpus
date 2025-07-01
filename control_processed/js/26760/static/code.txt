function addChainableConstructors() {
        var match = fnPackage.name.match(/^set(\w+)ChainableConstructor$/);
        if (match) {
          var namespace = match[1];
          var createPackage = sourcePackages.find(function(p) {
            return p.name === 'create' && p.namespace === namespace;
          });
          createPackage.dependencies.push(fnPackage.name);
        }
      }