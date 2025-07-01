function parseDate(s) {
    var date = new Date (s);
    return isNaN (date.valueOf ()) ? Nothing : Just (date);
  }