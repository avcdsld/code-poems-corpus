function getNormalizedV8Flag(arg) {
  // v8 uses the "no" prefix to negate boolean flags (e.g. --nolezy),
  // but they are not listed by v8flags
  const matches = arg.match(/--(?:no)?(.+)/);

  if (matches) {
    return `--${matches[1].replace(/-/g, "_")}`;
  }

  return arg;
}