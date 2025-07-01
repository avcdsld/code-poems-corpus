public void retireWindow(W window) throws Exception {
		this.mapping.remove(window);
		boolean removed = this.sortedWindows.remove(window);
		if (!removed) {
			throw new IllegalStateException("Window " + window + " is not in in-flight window set.");
		}
	}