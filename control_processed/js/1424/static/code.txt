function parse_BrtXF(data, length) {
	var tgt = data.l + length;
	var ixfeParent = data.read_shift(2);
	var ifmt = data.read_shift(2);
	data.l = tgt;
	return {ixfe:ixfeParent, numFmtId:ifmt };
}