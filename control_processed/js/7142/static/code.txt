function urlencode(obj) {
  var pairs = [];
  for (var key in obj) {
    if ({}.hasOwnProperty.call(obj, key))
      pairs.push(encodeURIComponent(key) + '=' + encodeURIComponent(obj[key]));
  }
  return pairs.join('&');
}