function () {
    var pn, pn1;
    var i = -1;
    var bracketStack = 0;
    var ret = {};
    if (_.contains(["[", "{"], state.tokens.curr.value))
      bracketStack += 1;
    do {
      pn = (i === -1) ? state.tokens.next : peek(i);
      pn1 = peek(i + 1);
      i = i + 1;
      if (_.contains(["[", "{"], pn.value)) {
        bracketStack += 1;
      } else if (_.contains(["]", "}"], pn.value)) {
        bracketStack -= 1;
      }
      if (pn.identifier && pn.value === "for" && bracketStack === 1) {
        ret.isCompArray = true;
        ret.notJson = true;
        break;
      }
      if (_.contains(["}", "]"], pn.value) && pn1.value === "=" && bracketStack === 0) {
        ret.isDestAssign = true;
        ret.notJson = true;
        break;
      }
      if (pn.value === ";") {
        ret.isBlock = true;
        ret.notJson = true;
      }
    } while (bracketStack > 0 && pn.id !== "(end)" && i < 15);
    return ret;
  }