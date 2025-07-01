public boolean matchesToken(String tokenName, HttpCookie cookie) {
		// Check if the cookie is null
		if (cookie == null) {
			return tokenValues.containsKey(tokenName) ? false : true;
		}

		// Check the value of the token from the cookie
		String tokenValue = getTokenValue(tokenName);
		if (tokenValue != null && tokenValue.equals(cookie.getValue())) {
			return true;
		}
		return false;
	}