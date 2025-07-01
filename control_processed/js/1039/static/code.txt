function formatArgs(firstArg, ...args) {
  if (typeof firstArg === 'function') {
    firstArg = firstArg();
  }
  if (typeof firstArg === 'string') {
    args.unshift(`deck.gl ${firstArg}`);
  } else {
    args.unshift(firstArg);
    args.unshift('deck.gl');
  }
  return args;
}