function isParameter(sSegment, oOverload) {
				var aMatches;

				if (sSegment && oOverload.$Parameter) {
					aMatches = oOverload.$Parameter.filter(function (oParameter) {
						return oParameter.$Name === sSegment;
					});
					if (aMatches.length) { // there can be at most one match
						// Note: annotations at parameter are handled before this method is called
						// @see annotationAtParameter
						vResult = aMatches[0];

						return true;
					}
				}

				return false;
			}