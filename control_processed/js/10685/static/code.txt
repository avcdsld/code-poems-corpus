function before(args) {
    const source = args.source;
    const index = args.index;
    const err = args.err;
    const errTarget = args.errTarget;
    const lineCheckStr = args.lineCheckStr;
    const onlyOneChar =
      args.onlyOneChar === undefined ? false : args.onlyOneChar;
    const allowIndentation =
      args.allowIndentation === undefined ? false : args.allowIndentation;

    activeArgs = {
      source,
      index,
      err,
      errTarget,
      onlyOneChar,
      allowIndentation
    };

    switch (expectation) {
      case "always":
        expectBefore();
        break;
      case "never":
        rejectBefore();
        break;
      case "always-single-line":
        if (!isSingleLineString(lineCheckStr || source)) {
          return;
        }

        expectBefore(messages.expectedBeforeSingleLine);
        break;
      case "never-single-line":
        if (!isSingleLineString(lineCheckStr || source)) {
          return;
        }

        rejectBefore(messages.rejectedBeforeSingleLine);
        break;
      case "always-multi-line":
        if (isSingleLineString(lineCheckStr || source)) {
          return;
        }

        expectBefore(messages.expectedBeforeMultiLine);
        break;
      case "never-multi-line":
        if (isSingleLineString(lineCheckStr || source)) {
          return;
        }

        rejectBefore(messages.rejectedBeforeMultiLine);
        break;
      default:
        throw configurationError(`Unknown expectation "${expectation}"`);
    }
  }