function addInt(x, n) {
  var ans=expand(x, x.length+1);
  addInt_(ans, n);
  return trim(ans, 1);
}