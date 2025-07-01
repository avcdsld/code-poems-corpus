function () {
  var args = Array.prototype.slice.call(arguments);
  console.error();
  console.error.apply(console, [" "].concat(args));
  console.error();
  process.exit(1); // eslint-disable-line no-process-exit
}