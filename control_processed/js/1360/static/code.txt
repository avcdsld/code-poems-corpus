function parse_VtVecUnalignedLpstrValue(blob) {
	var length = blob.read_shift(4);
	var ret = [];
	for(var i = 0; i != length; ++i) ret[i] = blob.read_shift(0, 'lpstr-cp').replace(chr0,'');
	return ret;
}