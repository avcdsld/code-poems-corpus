function handleTabCounts(str, freezeTabs) {
  var result;
  if (_.isArray(str)) {
    this._tabCtr += 1;
    if (this._tabCtr > 1) {
      result = str.length === 0 ? undefined : str;
    }
  } else {
    this._tabCtr = freezeTabs === true ? this._tabCtr + 1 : 0;
    result = str;
  }
  return result;
}