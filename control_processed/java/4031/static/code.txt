public static FixedDelayRestartStrategyFactory createFactory(Configuration configuration) throws Exception {
		int maxAttempts = configuration.getInteger(ConfigConstants.RESTART_STRATEGY_FIXED_DELAY_ATTEMPTS, 1);

		String delayString = configuration.getString(ConfigConstants.RESTART_STRATEGY_FIXED_DELAY_DELAY);

		long delay;

		try {
			delay = Duration.apply(delayString).toMillis();
		} catch (NumberFormatException nfe) {
			throw new Exception("Invalid config value for " +
					ConfigConstants.RESTART_STRATEGY_FIXED_DELAY_DELAY + ": " + delayString +
					". Value must be a valid duration (such as '100 milli' or '10 s')");
		}

		return new FixedDelayRestartStrategyFactory(maxAttempts, delay);
	}