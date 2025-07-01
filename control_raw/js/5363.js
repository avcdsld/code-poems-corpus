function createEvent (rgx, evtName, wholeMatch, text, id, url, title, options, globals) {
    return globals.converter._dispatch(evtName, wholeMatch, options, globals, {
      regexp: rgx,
      matches: {
        wholeMatch: wholeMatch,
        text: text,
        id: id,
        url: url,
        title: title
      }
    });
  }