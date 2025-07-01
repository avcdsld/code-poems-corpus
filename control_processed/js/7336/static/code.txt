function decodeCssEscape(s) {
    var i = parseInt(s.substring(1), 16);
    // If parseInt didn't find a hex diigt, it returns NaN so return the
    // escaped character.
    // Otherwise, parseInt will stop at the first non-hex digit so there's no
    // need to worry about trailing whitespace.
    if (i > 0xffff) {
      // A supplemental codepoint.
      return i -= 0x10000,
        String.fromCharCode(
            0xd800 + (i >> 10),
            0xdc00 + (i & 0x3FF));
    } else if (i == i) {
      return String.fromCharCode(i);
    } else if (s[1] < ' ') {
      // "a backslash followed by a newline is ignored".
      return '';
    } else {
      return s[1];
    }
  }