function(content, pos, sanitize) {
			if (sanitize) {
				content = this.sanitize(content);
			}

			var skipString = function() {
				var quote = content.charAt(pos);
				if (quote == '"' || quote == "'") {
					while (--pos >= 0) {
						if (content.charAt(pos) == quote && content.charAt(pos - 1) != '\\') {
							break;
						}
					}
					return true;
				}

				return false;
			};

			// find CSS selector
			var ch;
			var endPos = pos;
			while (--pos >= 0) {
				if (skipString()) continue;

				ch = content.charAt(pos);
				if (ch == ')') {
					// looks like it’s a preprocessor thing,
					// most likely a mixin arguments list, e.g.
					// .mixin (@arg1; @arg2) {...}
					while (--pos >= 0) {
						if (skipString()) continue;

						if (content.charAt(pos) == '(') {
							break;
						}
					}
					continue;
				}

				if (ch == '{' || ch == '}' || ch == ';') {
					pos++;
					break;
				}
			}

			if (pos < 0) {
				pos = 0;
			}
			
			var selector = content.substring(pos, endPos);

			// trim whitespace from matched selector
			var m = selector.replace(reSpace, ' ').match(reSpaceTrim);
			if (m) {
				pos += m[1].length;
				endPos -= m[2].length;
			}

			return range.create2(pos, endPos);
		}