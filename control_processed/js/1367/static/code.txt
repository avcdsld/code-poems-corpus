function parse_HyperlinkString(blob) {
	var len = blob.read_shift(4);
	var o = len > 0 ? blob.read_shift(len, 'utf16le').replace(chr0, "") : "";
	return o;
}