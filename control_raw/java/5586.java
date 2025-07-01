@Override
	public Iterable<T> get() throws Exception {
		Iterable<T> original = originalState.get();
		return original != null ? original : emptyState;
	}