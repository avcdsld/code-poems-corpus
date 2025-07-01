function verifyHeaders(headers) {
  for (let i = 0; i < headers.length; i++) {
    if (!/^([^\s:]|[^\s:][^:]*[^\s:]): .+$/.test(headers[i])) {
      throw new Error('Improperly formatted armor header: ' + headers[i]);
    }
    if (!/^(Version|Comment|MessageID|Hash|Charset): .+$/.test(headers[i])) {
      util.print_debug_error(new Error('Unknown header: ' + headers[i]));
    }
  }
}