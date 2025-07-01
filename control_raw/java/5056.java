private static LocalEnvironment createLocalEnvironment(Configuration configuration, int defaultParallelism) {
		final LocalEnvironment localEnvironment = new LocalEnvironment(configuration);

		if (defaultParallelism > 0) {
			localEnvironment.setParallelism(defaultParallelism);
		}

		return localEnvironment;
	}