function after(args) {
    const source = args.source;
    const index = args.index;
    const err = args.err;
    const errTarget = args.errTarget;
    const lineCheckStr = args.lineCheckStr;
    const onlyOneChar =
      args.onlyOneChar === undefined ? false : args.onlyOneChar;

    activeArgs = { source, index, err, errTarget, onlyOneChar };

    switch (expectation) {
      case "always":
        expectAfter();
        break;
      case "never":
        rejectAfter();
        break;
      case "always-single-line":
        if (!isSingleLineString(lineCheckStr || source)) {
          return;
        }

        expectAfter(messages.expectedAfterSingleLine);
        break;
      case "never-single-line":
        if (!isSingleLineString(lineCheckStr || source)) {
          return;
        }

        rejectAfter(messages.rejectedAfterSingleLine);
        break;
      case "always-multi-line":
        if (isSingleLineString(lineCheckStr || source)) {
          return;
        }

        expectAfter(messages.expectedAfterMultiLine);
        break;
      case "never-multi-line":
        if (isSingleLineString(lineCheckStr || source)) {
          return;
        }

        rejectAfter(messages.rejectedAfterMultiLine);
        break;
      default:
        throw configurationError(`Unknown expectation "${expectation}"`);
    }
  }