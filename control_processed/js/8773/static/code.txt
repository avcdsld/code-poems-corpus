function (sColor) {
				var sHexColor = "";

				if (!sColor || sColor.toLowerCase().indexOf("hsl") !== -1) {
					return undefined;
				}

				// named color
				if (sColor.indexOf("#") === -1) {
					return this.NAME_COLORS_TO_RGB_MAP[sColor.toLowerCase()] ? sColor.toLowerCase() : undefined;
				}

				//HEX value
				if (sColor.length === 4) {
					sHexColor = ["#", sColor[1], sColor[1], sColor[2], sColor[2], sColor[3], sColor[3]].join("");
				} else {
					sHexColor = sColor;
				}

				sHexColor = sHexColor.toUpperCase();

				return this.RGB_TO_NAMED_COLORS_MAP[sHexColor];
			}