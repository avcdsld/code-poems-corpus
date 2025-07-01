function pad(str) {
  if (str.length < max) {
    return str + ' '.repeat(max - str.length);
  }
  return str;
}