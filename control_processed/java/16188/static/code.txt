@Override
	public Bulkhead bulkhead(String name, BulkheadConfig config) {
		return computeIfAbsent(name, () -> Bulkhead.of(name, Objects.requireNonNull(config, CONFIG_MUST_NOT_BE_NULL)));
	}