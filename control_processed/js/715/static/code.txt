function formatOption(name, helpMsg) {
  var result = [];
  var options = IDENTATION + '--' + name;

  if (options.length > MAX_HELP_POSITION) {
    result.push(options);
    result.push('\n');
    result.push(wrapStr(helpMsg, TOTAL_WIDTH,
        repeatStr(' ', HELP_TEXT_POSITION)).join('\n'));
  } else {
    var spaceCount = HELP_TEXT_POSITION - options.length;
    options += repeatStr(' ', spaceCount) + helpMsg;
    result.push(options.substring(0, TOTAL_WIDTH));
    options = options.substring(TOTAL_WIDTH);
    if (options) {
      result.push('\n');
      result.push(wrapStr(options, TOTAL_WIDTH,
          repeatStr(' ', HELP_TEXT_POSITION)).join('\n'));
    }
  }

  return result.join('');
}