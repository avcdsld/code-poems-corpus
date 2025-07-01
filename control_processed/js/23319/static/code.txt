function(abbr) {
			abbr = abbr || '';
			
			var that = this;
			
			// find multiplier
			abbr = abbr.replace(/\*(\d+)?$/, function(str, repeatCount) {
				that._setRepeat(repeatCount);
				return '';
			});
			
			this.abbreviation = abbr;
			
			var abbrText = extractText(abbr);
			if (abbrText) {
				abbr = abbrText.element;
				this.content = this._text = abbrText.text;
			}
			
			var abbrAttrs = parseAttributes(abbr);
			if (abbrAttrs) {
				abbr = abbrAttrs.element;
				this._attributes = abbrAttrs.attributes;
			}
			
			this._name = abbr;
			
			// validate name
			if (this._name && !reValidName.test(this._name)) {
				throw new Error('Invalid abbreviation');
			}
		}