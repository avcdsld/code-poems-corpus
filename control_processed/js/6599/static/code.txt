function(formatCode) {
    // check if default format
    var index = NumFmtXform.getDefaultFmtId(formatCode);
    if (index !== undefined) return index;

    // check if already in
    index = this.index.numFmt[formatCode];
    if (index !== undefined) return index;


    index = this.index.numFmt[formatCode] = NUMFMT_BASE + this.model.numFmts.length;
    var xml = this.map.numFmt.toXml({id: index, formatCode: formatCode});
    this.model.numFmts.push(xml);
    return index;
  }