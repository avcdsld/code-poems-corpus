function getQualifier(sTerm, sExpectedTerm) {
		if (sTerm === sExpectedTerm) {
			return "";
		}
		if (sTerm.indexOf(sExpectedTerm) === 0 && sTerm[sExpectedTerm.length] === "#"
				&& sTerm.indexOf("@", sExpectedTerm.length) < 0) {
			return sTerm.slice(sExpectedTerm.length + 1);
		}
	}