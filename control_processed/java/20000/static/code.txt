private static boolean containsSection(String contents, String beginToken, String endToken) {
		int idxToken;
		if ((idxToken = contents.indexOf(beginToken)) == -1 || contents.indexOf(endToken) < idxToken) {
			return false;
		}
		return true;
	}