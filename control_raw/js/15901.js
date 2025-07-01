function values(strMap) {
    return Z.map (function(k) { return strMap[k]; }, Object.keys (strMap));
  }