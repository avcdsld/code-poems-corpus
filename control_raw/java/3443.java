@Override
	public DefaultConfigurableOptionsFactory configure(Configuration configuration) {
		for (String key : CANDIDATE_CONFIGS) {
			String newValue = configuration.getString(key, null);

			if (newValue != null) {
				if (checkArgumentValid(key, newValue)) {
					this.configuredOptions.put(key, newValue);
				}
			}
		}
		return this;
	}