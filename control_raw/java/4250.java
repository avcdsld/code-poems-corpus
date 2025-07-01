public static FileSystemFactory decorateIfLimited(FileSystemFactory factory, String scheme, Configuration config) {
		checkNotNull(factory, "factory");

		final ConnectionLimitingSettings settings = ConnectionLimitingSettings.fromConfig(config, scheme);

		// decorate only if any limit is configured
		if (settings == null) {
			// no limit configured
			return factory;
		}
		else {
			return new ConnectionLimitingFactory(factory, settings);
		}
	}