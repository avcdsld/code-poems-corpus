function get() {
  if (!moduleManager && getDefault) {
    moduleManager = getDefault();
  }
  asserts.assert(
      moduleManager != null, 'The module manager has not yet been set.');
  return moduleManager;
}