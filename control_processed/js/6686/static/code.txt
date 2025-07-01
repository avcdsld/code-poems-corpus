function initSymbols() {
  var i;
  var symlen = AMsymbols.length;
  for (i=0; i<symlen; i++) {
    if (AMsymbols[i].tex) {
      AMsymbols.push({input:AMsymbols[i].tex, 
        tag:AMsymbols[i].tag, output:AMsymbols[i].output, ttype:AMsymbols[i].ttype,
        acc:(AMsymbols[i].acc||false)});
    }
  }
  refreshSymbols();
}