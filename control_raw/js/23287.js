function(syntax, name, minScore) {
			var result = this.fuzzyFindMatches(syntax, name, minScore)[0];
			if (result) {
				return result.value.parsedValue;
			}
		}