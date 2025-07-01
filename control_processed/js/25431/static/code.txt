function check(node) {
    var url = node.url
    var reason

    if (identifiers.indexOf(url.toLowerCase()) !== -1) {
      reason =
        'Did you mean to use `[' +
        url +
        ']` instead of ' +
        '`(' +
        url +
        ')`, a reference?'

      file.message(reason, node)
    }
  }