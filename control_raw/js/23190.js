function(rule) {
			var offset = rule.valueRange(true).start;
			var nestedSections = this.findAllRules(rule.valueRange().substring(rule.source));
			nestedSections.forEach(function(section) {
				section.start += offset;
				section.end += offset;
				section._selectorEnd += offset;
				section._contentStart += offset;
			});
			return nestedSections;
		}