public ConfigOption<T> withDescription(final String description) {
		return withDescription(Description.builder().text(description).build());
	}