function writeParamsForRequestHeaders(entry, out, consumedParams) {
    const params = entry.params;

    if (!(typeof params.line === 'string') ||
        !(params.headers instanceof Array)) {
      // Unrecognized params.
      return;
    }

    // Strip the trailing CRLF that params.line contains.
    const lineWithoutCRLF = params.line.replace(/\r\n$/g, '');
    out.writeArrowIndentedLines([lineWithoutCRLF].concat(params.headers));

    consumedParams.line = true;
    consumedParams.headers = true;
  }