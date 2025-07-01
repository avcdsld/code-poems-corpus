function parse_fonts(t, styles, themes, opts) {
	styles.Fonts = [];
	var font = {};
	var pass = false;
	t[0].match(tagregex).forEach(function(x) {
		var y = parsexmltag(x);
		switch(strip_ns(y[0])) {
			case '<fonts': case '<fonts>': case '</fonts>': break;

			/* 18.8.22 font CT_Font */
			case '<font': case '<font>': break;
			case '</font>': case '<font/>':
				styles.Fonts.push(font);
				font = {};
				break;

			/* 18.8.29 name CT_FontName */
			case '<name': if(y.val) font.name = y.val; break;
			case '<name/>': case '</name>': break;

			/* 18.8.2  b CT_BooleanProperty */
			case '<b': font.bold = y.val ? parsexmlbool(y.val) : 1; break;
			case '<b/>': font.bold = 1; break;

			/* 18.8.26 i CT_BooleanProperty */
			case '<i': font.italic = y.val ? parsexmlbool(y.val) : 1; break;
			case '<i/>': font.italic = 1; break;

			/* 18.4.13 u CT_UnderlineProperty */
			case '<u':
				switch(y.val) {
					case "none": font.underline = 0x00; break;
					case "single": font.underline = 0x01; break;
					case "double": font.underline = 0x02; break;
					case "singleAccounting": font.underline = 0x21; break;
					case "doubleAccounting": font.underline = 0x22; break;
				} break;
			case '<u/>': font.underline = 1; break;

			/* 18.4.10 strike CT_BooleanProperty */
			case '<strike': font.strike = y.val ? parsexmlbool(y.val) : 1; break;
			case '<strike/>': font.strike = 1; break;

			/* 18.4.2  outline CT_BooleanProperty */
			case '<outline': font.outline = y.val ? parsexmlbool(y.val) : 1; break;
			case '<outline/>': font.outline = 1; break;

			/* 18.8.36 shadow CT_BooleanProperty */
			case '<shadow': font.shadow = y.val ? parsexmlbool(y.val) : 1; break;
			case '<shadow/>': font.shadow = 1; break;

			/* 18.8.12 condense CT_BooleanProperty */
			case '<condense': font.condense = y.val ? parsexmlbool(y.val) : 1; break;
			case '<condense/>': font.condense = 1; break;

			/* 18.8.17 extend CT_BooleanProperty */
			case '<extend': font.extend = y.val ? parsexmlbool(y.val) : 1; break;
			case '<extend/>': font.extend = 1; break;

			/* 18.4.11 sz CT_FontSize */
			case '<sz': if(y.val) font.sz = +y.val; break;
			case '<sz/>': case '</sz>': break;

			/* 18.4.14 vertAlign CT_VerticalAlignFontProperty */
			case '<vertAlign': if(y.val) font.vertAlign = y.val; break;
			case '<vertAlign/>': case '</vertAlign>': break;

			/* 18.8.18 family CT_FontFamily */
			case '<family': if(y.val) font.family = parseInt(y.val,10); break;
			case '<family/>': case '</family>': break;

			/* 18.8.35 scheme CT_FontScheme */
			case '<scheme': if(y.val) font.scheme = y.val; break;
			case '<scheme/>': case '</scheme>': break;

			/* 18.4.1 charset CT_IntProperty */
			case '<charset':
				if(y.val == '1') break;
				y.codepage = CS2CP[parseInt(y.val, 10)];
				break;

			/* 18.?.? color CT_Color */
			case '<color':
				if(!font.color) font.color = {};
				if(y.auto) font.color.auto = parsexmlbool(y.auto);

				if(y.rgb) font.color.rgb = y.rgb.slice(-6);
				else if(y.indexed) {
					font.color.index = parseInt(y.indexed, 10);
					var icv = XLSIcv[font.color.index];
					if(font.color.index == 81) icv = XLSIcv[1];
					if(!icv) throw new Error(x);
					font.color.rgb = icv[0].toString(16) + icv[1].toString(16) + icv[2].toString(16);
				} else if(y.theme) {
					font.color.theme = parseInt(y.theme, 10);
					if(y.tint) font.color.tint = parseFloat(y.tint);
					if(y.theme && themes.themeElements && themes.themeElements.clrScheme) {
						font.color.rgb = rgb_tint(themes.themeElements.clrScheme[font.color.theme].rgb, font.color.tint || 0);
					}
				}

				break;
			case '<color/>': case '</color>': break;

			/* 18.2.10 extLst CT_ExtensionList ? */
			case '<extLst': case '<extLst>': case '</extLst>': break;
			case '<ext': pass = true; break;
			case '</ext>': pass = false; break;
			default: if(opts && opts.WTF) {
				if(!pass) throw new Error('unrecognized ' + y[0] + ' in fonts');
			}
		}
	});
}