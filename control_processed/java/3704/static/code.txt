@PublicEvolving
	public double getDouble(ConfigOption<Double> configOption) {
		Object o = getValueOrDefaultFromOption(configOption);
		return convertToDouble(o, configOption.defaultValue());
	}