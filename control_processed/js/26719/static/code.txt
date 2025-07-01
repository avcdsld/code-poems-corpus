function(n) {
    var num = abs(n), last = +num.toString().slice(-2);
    return n + getOrdinalSuffix(last);
  }