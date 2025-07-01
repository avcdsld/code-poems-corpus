public void addHttpSessionToken(String site, String token) {
		// Add a default port
		if (!site.contains(":")) {
			site = site + (":80");
		}
		HttpSessionTokensSet siteTokens = sessionTokens.get(site);
		if (siteTokens == null) {
			siteTokens = new HttpSessionTokensSet();
			sessionTokens.put(site, siteTokens);
		}

		if (log.isDebugEnabled()) {
			log.debug("Added new session token for site '" + site + "': " + token);
		}

		siteTokens.addToken(token);
		// If the session token is a default token and was previously marked as remove, undo that
		unmarkRemovedDefaultSessionToken(site, token);
	}