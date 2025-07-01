private void init() {
		this.paused = false;
		this.stopped = true;
		this.tasksDoneCount = 0;
		this.tasksTotalCount = 0;
		this.initialized = false;

		// Add a default fetch filter and any custom ones
		defaultFetchFilter = new DefaultFetchFilter();
		this.addFetchFilter(defaultFetchFilter);
		
		for (FetchFilter filter : extension.getCustomFetchFilters()) {
			this.addFetchFilter(filter);
		}

		// Add a default parse filter and any custom ones
		this.addParseFilter(new DefaultParseFilter(spiderParam, extension.getMessages()));
		for (ParseFilter filter : extension.getCustomParseFilters())
			this.addParseFilter(filter);
		
		// Add the scan context, if any
		defaultFetchFilter.setScanContext(this.scanContext);
		defaultFetchFilter.setDomainsAlwaysInScope(spiderParam.getDomainsAlwaysInScopeEnabled());

	}