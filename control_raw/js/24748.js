function printWarning(format, ...args) {
  var argIndex = 0;
  var message = 'Warning: ' + format.replace(/%s/g, () => args[argIndex++]);
  if (typeof console !== 'undefined') {
    console.error(message);
  }
  try {
    // --- Welcome to debugging React ---
    // This error was thrown as a convenience so that you can use this stack
    // to find the callsite that caused this warning to fire.
    throw new Error(message);
  } catch (x) {}
}