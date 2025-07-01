function (oProperty) {
			var aMatches,
				sName,
				sQualifier,
				mValueLists = {};

			for (sName in oProperty) {
				aMatches = rValueList.exec(sName);
				if (aMatches){
					sQualifier = (aMatches[1] || "").slice(1); // remove leading #
					mValueLists[sQualifier] = oProperty[sName];
				}
			}

			return mValueLists;
		}