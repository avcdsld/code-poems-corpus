function(mAttributes, oNode) {
		var mIgnoredAttributes = {
				"Property" : true,
				"Qualifier": true,
				"Term": true,
				"xmlns" : true
			};

		for (var i = 0; i < oNode.attributes.length; i += 1) {
			var sName = oNode.attributes[i].name;
			if (!mIgnoredAttributes[sName] && (sName.indexOf("xmlns:") !== 0)) {
				var sValue = oNode.attributes[i].value;

				// Special case: EnumMember can contain a space separated list of properties that must all have their
				// aliases replaced
				if (sName === "EnumMember" && sValue.indexOf(" ") > -1) {
					var aValues = sValue.split(" ");
					mAttributes[sName] = aValues.map(AnnotationParser.replaceWithAlias).join(" ");
				} else {
					mAttributes[sName] = AnnotationParser.replaceWithAlias(sValue);
				}
			}
		}

		return mAttributes;
	}