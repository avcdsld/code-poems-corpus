function reformatHeaders(entry) {
    // If there are no headers, or it is not an object other than an array,
    // return |entry| without modification.
    if (!entry.params || entry.params.headers === undefined ||
        typeof entry.params.headers !== 'object' ||
        entry.params.headers instanceof Array) {
      return entry;
    }

    // Duplicate the top level object, and |entry.params|, so the original
    // object
    // will not be modified.
    entry = shallowCloneObject(entry);
    entry.params = shallowCloneObject(entry.params);

    // Convert headers to an array.
    const headers = [];
    for (const key in entry.params.headers) {
      headers.push(key + ': ' + entry.params.headers[key]);
    }
    entry.params.headers = headers;

    return entry;
  }