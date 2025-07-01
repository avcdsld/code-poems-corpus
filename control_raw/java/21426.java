public void setParseSVNEntries(boolean parseSVNentries) {
		this.parseSVNentries = parseSVNentries;
		getConfig().setProperty(SPIDER_PARSE_SVN_ENTRIES, Boolean.toString(parseSVNentries));
	}