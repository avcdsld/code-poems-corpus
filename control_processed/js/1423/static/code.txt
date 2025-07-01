function parse_BrtFont(data, length, opts) {
	var out = ({});

	out.sz = data.read_shift(2) / 20;

	var grbit = parse_FontFlags(data, 2, opts);
	if(grbit.fCondense) out.condense = 1;
	if(grbit.fExtend) out.extend = 1;
	if(grbit.fShadow) out.shadow = 1;
	if(grbit.fOutline) out.outline = 1;
	if(grbit.fStrikeout) out.strike = 1;
	if(grbit.fItalic) out.italic = 1;

	var bls = data.read_shift(2);
	if(bls === 0x02BC) out.bold = 1;

	switch(data.read_shift(2)) {
		/* case 0: out.vertAlign = "baseline"; break; */
		case 1: out.vertAlign = "superscript"; break;
		case 2: out.vertAlign = "subscript"; break;
	}

	var underline = data.read_shift(1);
	if(underline != 0) out.underline = underline;

	var family = data.read_shift(1);
	if(family > 0) out.family = family;

	var bCharSet = data.read_shift(1);
	if(bCharSet > 0) out.charset = bCharSet;

	data.l++;
	out.color = parse_BrtColor(data, 8);

	switch(data.read_shift(1)) {
		/* case 0: out.scheme = "none": break; */
		case 1: out.scheme = "major"; break;
		case 2: out.scheme = "minor"; break;
	}

	out.name = parse_XLWideString(data, length - 21);

	return out;
}