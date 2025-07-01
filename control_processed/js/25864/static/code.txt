function multMod(x, y, n) {
  var ans=expand(x, n.length);
  multMod_(ans, y, n);
  return trim(ans, 1);
}