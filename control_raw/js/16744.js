function normalizeDirectives (options) {
  const dirs = options.directives;
  if (dirs) {
    for (const key in dirs) {
      const def$$1 = dirs[key];
      if (typeof def$$1 === 'function') {
        dirs[key] = { bind: def$$1, update: def$$1 };
      }
    }
  }
}