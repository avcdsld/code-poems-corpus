function(content) {
			content = commentsUtils.strip(content);

			// remove preprocessor string interpolations like #{var}
			var stream = stringStream(content);
			var replaceRanges = [];
			var ch, ch2;

			while ((ch = stream.next())) {
				if (isQuote(ch)) {
					// skip string
					stream.skipString(ch)
					continue;
				} else if (ch === '#' || ch === '@') {
					ch2 = stream.peek();
					if (ch2 === '{') { // string interpolation
						stream.start = stream.pos - 1;

						if (stream.skipTo('}')) {
							stream.pos += 1;
						} else {
							throw 'Invalid string interpolation at ' + stream.start;
						}

						replaceRanges.push([stream.start, stream.pos]);
					}
				}
			}

			return utils.replaceWith(content, replaceRanges, 'a');
		}