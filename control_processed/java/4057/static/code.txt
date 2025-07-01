public DBOptions getDbOptions() {
		// initial options from pre-defined profile
		DBOptions opt = getPredefinedOptions().createDBOptions();

		// add user-defined options factory, if specified
		if (optionsFactory != null) {
			opt = optionsFactory.createDBOptions(opt);
		}

		// add necessary default options
		opt = opt.setCreateIfMissing(true);

		return opt;
	}