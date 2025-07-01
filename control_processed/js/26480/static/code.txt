function(value)
	{
		var callback = function(m) {
			return new YamlUnescaper().unescapeCharacter(m);
		};

		// evaluate the string
		return value.replace(new RegExp(YamlUnescaper.REGEX_ESCAPED_CHARACTER, 'g'), callback);
	}