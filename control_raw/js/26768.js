function getPackagePath(p) {
      if (p.path) {
        return p.path;
      } else if (p.polyfill) {
        return path.join('polyfills', p.namespace.toLowerCase(), p.name);
      } else if (p.type === 'fix') {
        return path.join(p.module.toLowerCase(), 'fixes', p.name);
      } else if (p.type === 'locale') {
        return path.join(p.module.toLowerCase(), p.code);
      } else if (sourcePackageIsDependency(p)) {
        return path.join(p.module.toLowerCase(), p.type, p.name);
      } else {
        return path.join(p.namespace.toLowerCase(), p.name);
      }
    }